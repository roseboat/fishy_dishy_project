# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from fishydishy.models import Fish, Recipe, Review, UserProfile
from django.contrib.auth.models import User
from fishydishy.forms import UserForm, UserProfileForm, RecipeForm, CommentForm, FeedbackForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.mail import send_mail
from datetime import datetime
import json
from django.db.models import Q
from django.db.models import Avg


# Create your views here.
def index(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    request.session.set_test_cookie()
    recipe_list = Recipe.objects.order_by('-avgRating')[:5]

    context_dict = {'recipes': recipe_list}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    # Obtain our respnse object early so we can add cookie information
    response = render(request, 'fishydishy/index.html', context=context_dict)

    # call the helper function to handle the cookies
    # Return response back to the user, updating any cookies that need changed
    return response

    # return HttpResponse("Rango says hey there partner! <br/> <a href='/rango/about/'>About</a>")


def about(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()
    context_dict = {'boldmessage': "The king of cats"}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'fishydishy/about.html', context=context_dict)
    # return HttpResponse("Rango says here is the about page!<br/> <a href='/rango/'>Index</a>")
    # return render(request, 'rango/about.html', context=context_dict)
    return response


def fish_finder(request):
    fish_list = Fish.objects.order_by('name')

    context_dict = {'fishList': fish_list}

    response = render(request, 'fishydishy/fish_finder.html', context=context_dict)

    return response


def fish_map(request):
    response = render(request, 'fishydishy/fish_map.html')
    return response

def recipes(request):
    recipe_list = Recipe.objects.order_by('name')

    fish_list = Fish.objects.order_by('name')
    context_dict = {'recipeList': recipe_list,
                    'fishList': fish_list}

    response = render(request, 'fishydishy/recipes.html', context=context_dict)

    return response


def show_recipe(request, recipe_name_slug, *args, **kwargs):
    context_dict= {}

    try:
        
        recipe = Recipe.objects.get(slug=recipe_name_slug)
        reviews = Review.objects.filter(recipe=recipe).order_by('-date_posted')
        scoreAvg = Review.objects.filter(recipe=recipe).aggregate(Avg('rating'))['rating__avg']
        if scoreAvg is None:
            scoreRange = range(0,0)
        else:
            scoreRange = range(1, int(scoreAvg)+1)
        form = CommentForm()

        context_dict['reviews'] = reviews

        if request.method == 'POST':
            # user posted the form
            
            form.recipe = recipe
            form = CommentForm(request.POST)
            
            if form.is_valid():
                a = form.save(commit=False)
                a.recipe=Recipe.objects.get(slug=recipe_name_slug)
                a.user = request.user
                a.save()


                info_dict = {"comment": a.comment, "user": request.user.username, "date": a.date_posted.strftime('%B %d, %Y, %I:%M %p')}
                #info_dict = form.cleaned_data
                #username = request.user.username
                #info_dict['user'] = username
                return HttpResponse(json.dumps(info_dict), content_type="application/json")
                #return show_recipe(request, recipe_name_slug)
            else:
                print(form.errors)

            # process the form here. is it valid? save the form to the database.

    except Recipe.DoesNotExist:

        context_dict['recipe'] = None
        context_dict['reviews'] = None

    context_dict = {'form': form, 'recipe': recipe, 'reviews':reviews, 'scoreRange' : scoreRange}
    return render(request, 'fishydishy/recipe.html', context_dict)

def search(request):
    context_dict= {}
    if request.method == 'GET': # this will be GET now      
        target =  request.GET.get('search') # do some research what it does
        print(target, 'PRRIIIIIIIIIIIIIIIIIIIIIIIIIIIIIINT')
        try:
            recipeSearch = Recipe.objects.filter(description__icontains=target) | Recipe.objects.filter(name__icontains=target) | Recipe.objects.filter(fish__name__startswith=target) # filter returns a list so you might consider skip except part
            fishSearch = Fish.objects.filter(name__icontains=target) | Fish.objects.filter(description__icontains=target) | Fish.objects.filter(fishType__icontains=target)
            context_dict['recipeSearch'] = recipeSearch
            context_dict['fishSearch'] = fishSearch           
        except Recipe.DoesNotExist:
            print(error)
        return render(request,"fishydishy/search.html",context_dict)
    else:
        return render(request,"fishydishy/search.html",context_dict)



@login_required
def add_recipe(request, *args, **kwargs):
    print(request.POST)
    form = RecipeForm()
    print(request.user)

    
    # HTTP POST
    if request.method == 'POST': 
        form = RecipeForm(request.POST, request.FILES)

        print(form.errors.as_data())

        #user=
        recipe= Recipe(user=request.user.username)
        form= RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            # save new cate to DB
            recipe.save()
            
            # could give a confirmation message
            # but recent category is added on index page
            # and direct user back to index page
            
            return index(request)
        else:
            print(form.errors)

   # context_dict = {'form': form}
    return render(request, 'fishydishy/add_recipe.html', {'form': form})


def register(request):
    # A boolean value for telling the template whether the registration
    # was successful. Set to false initially. code changes value to true
    # when registration succeeds.
    registered = False

    # If its a HTTP POST, we interested in processing form data
    if request.method == 'POST':
        # Attempt to grab info from the raw form information
        # Note that we make use of both Userform and UserProfileForm
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)


        # If the two forms are valid then..
        if user_form.is_valid() and profile_form.is_valid():
            # Save the users form data to database
            user = user_form.save()

            # now hash password with set_password metthod
            # Once hashed, we can update the user object
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance
            # Since we need to set the user attribute ourselves
            # we set commit=False. This delays saving the model
            # until we ready to avoid integrity problems
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile pic?
            # If so, we need to get it from the input form and
            # put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance
            profile.save()

            # Update our variable to indicate that the template
            # registration was successful
            registered = True

        else:
            # invalid form or forms- mistakes or something else?
            # print problems to terminal.
            print(user_form.errors, profile_form.errors)
    else:
        # not a HTTP POST, so we render our form using two ModelForm instances.
        # These forms will be blank, ready for user input.
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on context.
    return render(request,
                  'fishydishy/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    # if the request is a HTTP POST, try to pull out the relevant information
    if request.method == 'POST':
        # Gather the username and password provided by the user
        # This information is obtained from the login form
        # We use request.POST.get('<variable>') as opposed
        # to request.POST{'<variable>'}, because the
        # request.POST.get('<varibale>') returns None if the
        # value does not exist, while the second one will raise
        # a KeyError exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Djanjos machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is
        user = authenticate(username=username, password=password)

        # if we have a User object, the detials are correct.
        # If None, no user with mathcing credentials was found.
        if user:
            # is the account active? it could have been disabled
            if user.is_active:
                # If the account is valid and active, we can log the user in
                # We'll send the user back to the homepage
                login(request, user)
                return HttpResponseRedirect(reverse('user_profile'))
            else:
                # An inactive account was used - no logging in
                return HttpResponse("Your Fishy Dishy account is disabled.")
        else:
            # bad login details were provided. So we cant log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenerio would most likely be a HTTP GET.
    else:
        # No contect variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'fishydishy/login.html', {})


@login_required
def user_profile(request):
    u = User.objects.get(id=1)
    u_p = u.userprofile
    context_dict = {}
    recipe_list = Recipe.objects.filter(user=request.user.username)

    # userStuff = UserProfile.objects.get(user=request.user)
    # context_dict['userStuff'] = userStuff

    userStuff = u_p
    context_dict['userStuff'] = userStuff
    context_dict['recipes'] = recipe_list

    return render(request, 'fishydishy/user_profile.html', context_dict)

def site_map(request):
    return render(request, 'fishydishy/site_map.html')


# Use the login_required decorator to ensure only those logged in can
# access the view
@login_required
def user_logout(request):
    # Since we know the user is loggin in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage
    return HttpResponseRedirect(reverse('index'))


# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


# Updated the function definition
def visitor_cookie_handler(request):
    # Get the number of visits to the site.
    # we use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesnt exist, then the default value of 1 is used.
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                               'last_visit',
                                               str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    # If its been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:

        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['fishy.dishy5@gmail.com']

            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)

            return index(request)
    else:
        form = FeedbackForm()
    response = render(request, 'fishydishy/contact.html', {'form':form})
    return response

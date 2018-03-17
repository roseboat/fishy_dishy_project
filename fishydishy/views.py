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



def index(request):
    # Order the recipes by average rating in descending order.
    # Retrieve the top 5 only
    # passed to the template engine.


    recipe_list = Recipe.objects.order_by('-avgRating')[:5]

    context_dict = {'recipes': recipe_list}

    # Obtain our respnse object early so we can add cookie information
    response = render(request, 'fishydishy/index.html', context=context_dict)

    return response

def about(request):

    response = render(request, 'fishydishy/about.html')
    return response


def fish_finder(request):
    #Get all fish in alphabetical order
    fish_list = Fish.objects.order_by('name')

    context_dict = {'fishList': fish_list}

    response = render(request, 'fishydishy/fish_finder.html', context=context_dict)

    return response


def fish_map(request):
    response = render(request, 'fishydishy/fish_map.html')
    return response

def recipes(request):
    #Get all recipes and fish in alphabetical order
    recipe_list = Recipe.objects.order_by('name')

    fish_list = Fish.objects.order_by('name')
    context_dict = {'recipeList': recipe_list,
                    'fishList': fish_list}

    response = render(request, 'fishydishy/recipes.html', context=context_dict)

    return response

'''
Method to show the recipe, retrieves recipes, reviews amd average score from the database.
Users can comment on the recipes and that is sent as a post request. Ajax is used to automatically update
the comment section. The comment is sent as JSON back.
'''
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

            form.recipe = recipe
            form = CommentForm(request.POST)

            if form.is_valid():
                a = form.save(commit=False)
                a.recipe=Recipe.objects.get(slug=recipe_name_slug)
                a.user = request.user
                a.save()

                info_dict = {"comment": a.comment, "user": request.user.username, "date": a.date_posted.strftime('%B %d, %Y, %I:%M %p')}
                return HttpResponse(json.dumps(info_dict), content_type="application/json")

            else:
                print(form.errors)

    except Recipe.DoesNotExist:

        context_dict['recipe'] = None
        context_dict['reviews'] = None

    context_dict = {'form': form, 'recipe': recipe, 'reviews':reviews, 'scoreRange' : scoreRange}
    return render(request, 'fishydishy/recipe.html', context_dict)
'''
In-built search engine within the website, searches for either fish or recipes. Returns a separated list
of results in both categories.
'''
def search(request):
    context_dict= {}
    if request.method == 'GET':
        target =  request.GET.get('search')

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


'''
Allows the user to add a recipe to their profile  via the recipe form. Users
can submit a picture of their recipe as well. 
'''
@login_required
def add_recipe(request, *args, **kwargs):
    form = RecipeForm()

    if request.method == 'POST':
        recipe= Recipe(user=request.user.username)
        form = RecipeForm(request.POST, request.FILES, instance=recipe)

        if form.is_valid():
            recipe.save()
            return index(request)
        else:
            print(form.errors)

    return render(request, 'fishydishy/add_recipe.html', {'form': form})

'''
Registration view, form collects information for the userprofile and stores the 
results in the database.
'''
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            #Hash password
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'fishydishy/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

'''
User logs in to their account if invalid details supplied page is reloaded but if 
they have an account the user is authenticated and redirected to their profile
'''
def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        #Check if the user is valid
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('user_profile'))
            else:
                return HttpResponse("Your Fishy Dishy account is disabled.")
        else:
            return render(request, 'fishydishy/login.html', {'message':"Invalid login details supplied"})

    # The request is not a HTTP POST, so display the login form.
    # This scenerio would most likely be a HTTP GET.
    else:
        # No contect variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'fishydishy/login.html', {})

@login_required
def user_profile(request):
    context_dict = {}


    # Gets the user's profile object
    u_p = UserProfile.objects.get(user=request.user)

    # Gets the recipes created by the user
    recipe_list = Recipe.objects.filter(user=request.user.username)
    context_dict['userStuff'] = u_p
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

# Method for the contact page which allows users to send an email to Fishy Dishy administrators
def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            # sends user's inputs to the administrator's email
            recipients = ['fishy.dishy5@gmail.com']

            if cc_myself:
                recipients.append(sender)

            # Send the user's inputs to the administrator's email
            send_mail(subject, message, sender, recipients)

            return index(request)
    else:
        form = FeedbackForm()
    response = render(request, 'fishydishy/contact.html', {'form':form})
    return response

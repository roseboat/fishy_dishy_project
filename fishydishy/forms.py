from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from fishydishy.models import UserProfile, Recipe, Fish, Review

# Creates a form for the User's registration/login
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# Additional form takes a website and picture from the user for use in their user profile
class UserProfileForm(forms.ModelForm):
    # website = forms.URLField(help_text="Enter the name of your site", blank=True)
    picture = forms.ImageField(help_text="Upload a Profile Picture")

    class Meta:
        model = UserProfile
        fields = ('picture',)

# Form for uploading a recipe to the website
class RecipeForm(forms.ModelForm):

    # gets the user who is inputting the recipe
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(RecipeForm, self).__init__(*args, **kwargs)

    name = forms.CharField(max_length=2000, help_text="Name your dish", widget=forms.Textarea(attrs={'cols': 60, 'rows': 1}))
    description = forms.CharField(max_length=2000, help_text="Description", widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    ingredients = forms.CharField(max_length=5000, help_text="Enter your ingredients", widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))
    method = forms.CharField(max_length=5000, help_text="Enter your method", widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))

    # Gets all of the fish from the website's database for use in a dropdown menu
    fish = forms.ModelChoiceField(queryset=Fish.objects.all(),to_field_name="name", initial=0, help_text="Which fish does it use?")
    serves = forms.IntegerField(help_text="How many servings?", min_value=1, max_value=10)
    time = forms.IntegerField(help_text="How long will it take? (mins)", min_value=1, max_value=999)
    image = forms.ImageField(help_text="Upload an Image of Your Dish")

    # Adds the inputs to the Recipe model
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients', 'method', 'fish', 'serves', 'time', 'image')
        exclude = ('user',)

# Form for users to leave a comment and a rating on a recipe
class CommentForm(forms.ModelForm):

    # Gets the user who is posting the comment
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    # fields for a comment
    comment = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    rating = forms.IntegerField(help_text="Rate this Recipe", min_value=1, max_value=5)

    # adds the inputs to the Review model
    class Meta:
        model = Review
        fields = ('comment', 'rating')
        exclude = ('user', 'recipe')

# Form for a user to contact the owners of the website
class FeedbackForm(forms.Form):
    subject = forms.CharField(help_text="Subject", max_length=100)
    message = forms.CharField(help_text="Message", widget=forms.Textarea)
    sender = forms.EmailField(help_text="Email Address")
    cc_myself = forms.BooleanField(help_text="Want to be CC'ed?", required=False)

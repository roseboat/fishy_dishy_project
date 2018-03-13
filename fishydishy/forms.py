from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from fishydishy.models import Page, Category, UserProfile, Recipe, Fish, Review

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    #other fields available such as EmailField, ChoiceField(radio buttons), DateField
    # An inline class to privide additional info on the form
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial =0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page
        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form
        exclude = ('category',)
        # or specify the fields to include (ie not include the category field)
        # fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # if url is not empty and doesnt start with http://
        # then prepend http://
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

class RecipeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user',None)
        super(RecipeForm, self).__init__(*args, **kwargs)

    name = forms.CharField(max_length=2000, help_text="Name your dish", widget=forms.Textarea(attrs={'cols': 60, 'rows': 1}))
    description = forms.CharField(max_length=2000, help_text="Description", widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    ingredients = forms.CharField(max_length=125, help_text="Enter your ingredients", widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))
    method = forms.CharField(max_length=300, help_text="Enter your method", widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}))
    fish = forms.ModelChoiceField(queryset=Fish.objects.all(),to_field_name="name", initial=0, help_text="Which fish does it use?") 
    serves = forms.CharField(max_length=125, help_text="How many servings?")
    #user = forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients', 'method', 'fish', 'serves')
        exclude = ('user',)

class CommentForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CommentForm, self).__init__(*args, **kwargs)

    comment = forms.CharField(max_length=2000, help_text="Review", widget=forms.Textarea(attrs={'cols': 60, 'rows': 3}))
    rating = forms.IntegerField()

    class Meta:
        model = Review
        fields = ('comment', 'rating')
        exclude = ('user', 'recipe')

class FeedbackForm(forms.Form):
    subject = forms.CharField(label='Subject', max_length=100)
    message = forms.CharField(label='Message', widget=forms.Textarea)
    sender = forms.EmailField(label='Email')
    cc_myself = forms.BooleanField(required=False)

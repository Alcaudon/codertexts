from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Textarea, TextInput, EmailInput, PasswordInput
from users.models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=TextInput(attrs={'class': 'full-width'}))
    last_name = forms.CharField(required=False, widget=TextInput(attrs={'class': 'full-width'}))
    username = forms.CharField(max_length=30, required=True, widget=TextInput(attrs={'class': 'full-width'}))
    password1 = forms.CharField(required=True, widget=PasswordInput(attrs={'class': 'full-width'}))
    password2 = forms.CharField(required=True, widget=PasswordInput(attrs={'class': 'full-width'}))
    email = forms.EmailField(max_length=254, required=True, widget=EmailInput(attrs={'class': 'full-width'}))
    instagram_user = forms.CharField(required=False, widget=TextInput(attrs={'class': 'full-width'}))
    twitter_user = forms.CharField(required=False, widget=TextInput(attrs={'class': 'full-width'}))
    facebook_user = forms.CharField(required=False, widget=TextInput(attrs={'class': 'full-width'}))
    about_me = forms.CharField(required=True, widget=Textarea(attrs={'rows': 1, 'class': 'full-width'}))

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'password1',
                  'password2',
                  'email',
                  'instagram_user',
                  'twitter_user',
                  'facebook_user',
                  'about_me']


class LoginForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'class': 'full-width'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'full-width'}))

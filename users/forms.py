from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import Textarea, TextInput, EmailInput, PasswordInput

from users.models import User


class SignupForm(UserCreationForm):
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
        widgets = {
                   "first_name": TextInput(attrs={'class': 'full-width'}),
                   "last_name": TextInput(attrs={'class': 'full-width'}),
                   "username": TextInput(attrs={'class': 'full-width'}),
                   "email": EmailInput(attrs={'class': 'full-width'}),
                   "password1": PasswordInput(attrs={'class': 'full-width'}),
                   "password2": PasswordInput(attrs={'class': 'full-width'}),
                   "instagram_user": TextInput(attrs={'class': 'full-width'}),
                   "twitter_user": TextInput(attrs={'class': 'full-width'}),
                   "facebook_user": TextInput(attrs={'class': 'full-width'}),
                   "about_me": Textarea(attrs={'rows': 1, 'class': 'full-width'}),
                   }


class LoginForm(forms.Form):
    username = forms.CharField(widget=TextInput(attrs={'class': 'full-width'}))
    password = forms.CharField(widget=PasswordInput(attrs={'class': 'full-width'}))

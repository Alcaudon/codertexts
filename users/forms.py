from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import User


class SignupForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'password1',
                  'password2',
                  'instagram_user',
                  'twitter_user',
                  'facebook_user',
                  'about_me']
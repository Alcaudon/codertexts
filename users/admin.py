from django.contrib import admin
from users.models import Follower, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Follower)
admin.site.register(User, UserAdmin)
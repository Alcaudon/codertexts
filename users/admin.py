from django.contrib import admin

from users.models import Follower, User

admin.site.register(Follower)
admin.site.register(User)
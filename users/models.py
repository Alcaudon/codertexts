from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=25)
    image = models.URLField(blank=True)
    instagram_user = models.CharField(max_length=30, blank=True)
    twitter_user = models.CharField(max_length=30, blank=True)
    facebook_user = models.CharField(max_length=30, blank=True)
    about_me = models.CharField(max_length=140, blank=True)


class Follower(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users")
    id_follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        verbose_name_plural = "followers"

    def __str__(self):
        return str(self.id_user) + " - " + str(self.id_follower)
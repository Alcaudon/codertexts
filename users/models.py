from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.URLField(blank=True, null=True)
    instagram_user = models.CharField(max_length=30, blank=True, null=True)
    twitter_user = models.CharField(max_length=30, blank=True, null=True)
    facebook_user = models.CharField(max_length=30, blank=True, null=True)
    about_me = models.CharField(max_length=140, blank=True, null=True)


class Follower(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users")
    id_follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "followers"

    def __str__(self):
        return str(self.id_user) + " - " + str(self.id_follower)


# This code is triggered whenever a new user has been created and saved to the database
#@receiver(post_save, sender=settings.AUTH_USER_MODEL)
#def create_auth_token(sender, instance=None, created=False, **kwargs):
#    if created:
#        Token.objects.create(user=instance)
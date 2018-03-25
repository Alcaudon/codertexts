from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    image = serializers.URLField(allow_null=True, allow_blank=True)
    instagram_user = serializers.CharField(allow_null=True, allow_blank=True)
    twitter_user = serializers.CharField(allow_null=True, allow_blank=True)
    facebook_user = serializers.CharField(allow_null=True, allow_blank=True)
    about_me = serializers.CharField(allow_null=True, allow_blank=True)

    def validate_username(self, data):
        if User.objects.filter(username=data).exists():
            raise ValidationError("El usuario ya existe")
        return data

    def validate_email(self, data):
        if User.objects.filter(email=data).exists():
            raise ValidationError("El correo ya ha sido utilizado con anterioridad")
        return data

    def create(self, validated_data):
        instance = User()
        instance.first_name = validated_data.get("first_name")
        instance.last_name = validated_data.get("last_name")
        instance.username = validated_data.get("username")
        instance.email = validated_data.get("email")
        instance.set_password(validated_data.get("password"))
        instance.image = validated_data.get("image")
        instance.instagram_user = validated_data.get("instagram_user")
        instance.twitter_user = validated_data.get("twitter_user")
        instance.facebook_user = validated_data.get("facebook_user")
        instance.about_me = validated_data.get("about_me")
        instance.save()
        return instance

    def update(self, instance, validated_data):
        pass

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def validate_username(self, data):
        if self.instance is None and User.objects.filter(username=data).exists():
            raise ValidationError("El usuario ya existe")
        if self.instance and self.instance.username != data and User.objects.filter(username=data).exists():
            raise ValidationError("El nombre de usuario está ya en uso.")
        return data

    def validate_email(self, data):
        if self.instance is None and User.objects.filter(email=data).exists():
            raise ValidationError("El correo de usuario está ya en uso.")
        if self.instance and self.instance.email != data and User.objects.filter(email=data).exists():
            raise ValidationError("El correo de usuario está ya en uso.")
        return data

    def create(self, validated_data):
        instance = User()
        return self.update(instance, validated_data)

    def update(self, instance, validated_data):
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

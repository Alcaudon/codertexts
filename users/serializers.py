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

from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPI(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPI (UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteAPI (DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


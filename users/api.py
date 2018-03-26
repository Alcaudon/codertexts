from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from users.models import User
from users.permissions import UserPermissions
from users.serializers import UserSerializer


class UserCreateAPI(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateAPI (UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class UserDeleteAPI (DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]

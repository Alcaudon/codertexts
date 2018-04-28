from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView

from users.authentication import TokenAuthentication
from users.models import User
from users.permissions import UserPermissions
from users.serializers import UserSerializer


class UserCreateAPI(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class UserUpdateAPI (UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermissions]


class UserDeleteAPI (DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermissions]

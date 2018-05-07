from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import logout as django_logout
from django.db.models import Q

from users.authentication import TokenAuthentication
from users.models import User
from users.permissions import UserPermissions
from users.serializers import UserSerializer, RecuperarPasswordSerializer



class UserListAPI(ListAPIView):

    serializer_class = UserSerializer
    permission_classes = [UserPermissions]

    def get_queryset(self):
        id_user = self.request.user.id
        queryset = User.objects.filter(id=id_user)
        return queryset

class UserCreateAPI(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class UserUpdateAPI (UpdateAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [UserPermissions]


class UserDeleteAPI (DestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [UserPermissions]


class RecuperarUsuarioAPI(APIView):

    def post(self, request):
        usuario = User.objects.filter(Q(username=request.data['user']) | Q(email=request.data['user']))
        if usuario:
            serializer = RecuperarPasswordSerializer(usuario, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK, content_type="application/json")
        else:
            return Response(data=False, status=status.HTTP_200_OK)


class Logout(APIView):

    def get(self, request):
        # simply delete the token to force a login
        django_logout(request)
        return Response(status=status.HTTP_200_OK)

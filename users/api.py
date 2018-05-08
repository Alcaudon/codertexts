from rest_framework import status
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import logout as django_logout
from django.db.models import Q

#from users.authentication import TokenAuthentication
from users.models import User
from users.permissions import UserPermissions
from users.serializers import UserSerializer, RecuperarPasswordSerializer


class UserDetailAPI(APIView):
    """Devuelve los datos de un usuario del sistema"""
    permission_classes = [UserPermissions]
    serializer_class = UserSerializer

    def get(self, request):
        id_user = self.request.user.id
        usuario = User.objects.filter(id=id_user)
        if usuario:
            serializer = UserSerializer(usuario, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK, content_type="application/json")
        return Response(data=False, status=status.HTTP_200_OK)

class UserCreateAPI(CreateAPIView):
    """Crear un usuario"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class UserUpdateAPI (UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermissions]


class UserDeleteAPI (DestroyAPIView):

    serializer_class = UserSerializer
    permission_classes = [UserPermissions]

    def destroy(self, request):
        id_user = self.request.user.id
        instance = User.objects.filter(id=id_user)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class RecuperarPasswordAPI(APIView):

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

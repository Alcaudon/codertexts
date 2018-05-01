import jwt
from django.contrib.auth import login
from django.utils.deprecation import MiddlewareMixin
from rest_framework_jwt.authentication import jwt_decode_handler

from users.models import User


class LoginCheckMiddleware(MiddlewareMixin):

    def process_view(self, request, callback, callback_args, callback_kwargs):
        csrf_cookie = request.COOKIES.get('token')
        if csrf_cookie:
            usuario = self.authenticate_credentials(csrf_cookie)
            if usuario:
                login(request, usuario)
        return None

    def authenticate_credentials(self, token):
        payload = jwt_decode_handler(token)
        username = payload['username']
        email = payload['email']
        try:
            user = User.objects.get(
                username=username,
                email=email,
                is_active=True
            )
            if user:
                return user
        except jwt.ExpiredSignature or jwt.DecodeError or jwt.InvalidTokenError:
            return None
        except User.DoesNotExist:
            return None
        return None

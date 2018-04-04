from django.contrib.auth import authenticate
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
import jwt
from codertexts.settings import SECRET_KEY

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginUserView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            payload = jwt_payload_handler(user)
            token = {
                'token': jwt.encode(payload, SECRET_KEY),
                'status': 'success'
                }
            return Response(token)
        else:
            return Response(
              {'error': 'Invalid credentials', 'status': 'failed'}
            )


from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from rest_framework.views import APIView
from django.contrib import messages

from django.shortcuts import render, redirect
from django.views import View
from users.forms import SignupForm, LoginForm
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


class SignupView(View):

    def get(self, request):
        context = {'form': SignupForm()}
        return render(request, "signup_form.html", context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user and authenticated_user.is_active:
                django_login(request, authenticated_user)
            return redirect("home_page")
        else:
            messages.error(request, "Vuelva a intentarlo")
        return render(request, "signup_form.html", {'form': form})


class LoginView(View):

    def get(self, request):
        context = {'form': LoginForm()}
        return render(request, "login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user and authenticated_user.is_active:
                django_login(request, authenticated_user)
                redirect_to = request.GET.get("next", "home_page")
                return redirect(redirect_to)
            else:
                form.add_error(None, "Usuario incorrecto o inactivo")
        return render(request, "login.html", {'form': form})


def logout(request):
    django_logout(request)
    return redirect("home_page")

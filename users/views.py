from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from users.forms import SignupForm


class signupView(View):

    def get(self, request):
        context = {'form': SignupForm()}
        return render(request, "signup_form.html", context)

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")
        else:
            messages.error(request, "Vuelva a intentarlo")
        return render(request, "signup_form.html", {'form': form})

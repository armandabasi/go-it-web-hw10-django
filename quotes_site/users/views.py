from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView


class MyLoginView(LoginView):
    extra_context = {"title": "QuoteHive: login"}


class MyLogoutView(LogoutView):
    extra_context = {"title": "QuoteHive: logout"}


# Create your views here.
class RegisterView(View):
    form_class = RegisterForm
    template_name = "users/signup.html"

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class, "title": "QuoteHive: sign up"})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Welcome {username}. Your account has been successfully created!")
            return redirect(to="users:login")
        return render(request, self.template_name, context={"form": form, "title": "QuoteHive: sign up"})

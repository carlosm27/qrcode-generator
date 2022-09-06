from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView

# Create your views here.
def home_page(request):
	return render (request,"users/home.html")

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("home")
    template_name = "users/registration/signup.html"

class Login(LoginView):
    form_class = AuthenticationForm
    template_name = "users/registration/login.html"

class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = "users/registration/password_change_form.html"
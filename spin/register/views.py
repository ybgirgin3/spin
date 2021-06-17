"""# views.py
from django.shortcuts import render, redirect
from .forms import RegisterForm


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/login")
    else:
        form = RegisterForm()

        return render(response, "register/register.html", {"form":form})

"""

from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from .forms import LoginForm, RegisterForm
# Create your views here.

class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'

class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'register/register.html'
    success_url = reverse_lazy('login')

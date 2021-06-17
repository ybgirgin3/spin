from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=30)
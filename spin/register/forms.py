from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Hesap Anahtarı / Kullanıcı Adı')





"""
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Hesap Anahtarı / Kullanıcı Adı')
"""
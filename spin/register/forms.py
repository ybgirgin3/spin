from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')
        

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Hesap Anahtarı / Kullanıcı Adı')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
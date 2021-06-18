from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class RegisterForm(UserCreationForm):
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'phone_number', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Kullanıcı Adı')

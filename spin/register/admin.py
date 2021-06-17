"""from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import RegisterForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = RegisterForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]
    
admin.site.register(CustomUser, CustomUserAdmin)"""
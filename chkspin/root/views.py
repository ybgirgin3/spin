from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import Item, ItemSpec
from .forms import CreateNewItem

def home(response):
    return render(response, "root/home.html")
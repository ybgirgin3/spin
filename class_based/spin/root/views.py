from django.shortcuts import render
from posts.models import PostModel
from django.views.generic import ListView



class HomeView(ListView):
    model = PostModel
    template_name = 'root/home.html'


# # Create your views here.
# def home(response):
#     p = PostModel.objects.all()
#     return render(response, "root/home.html", {'posts': p})

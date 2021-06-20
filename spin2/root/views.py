from django.shortcuts import render
from posts.models import PostModel

# Create your views here.
def home(response):
    p = PostModel.objects.all()
    return render(response, "root/home.html", {'posts': p})
    # return render(response, "root/home.html")

"""
def list_all_view(response):
    p = PostModel.objects.all()
    return render(response, "posts/post_all.html", {'posts': p})
"""
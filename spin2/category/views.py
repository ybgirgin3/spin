from django.shortcuts import render
from .models import Category
from posts.models import PostModel
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def index_view(response):
    categories = Category.objects.all()
    return render(response, "category/categories.html", {"categories": categories})

def category_view(response):
    categoryChoose = Category.objects.get(slug=slug)
    postsList = PostModel.objects.filter(category=categoryChoose)
    paginator = Paginator(postsList, 2)
    page = response.GET.get('page')
    posts = paginator.get_page(page)
    return render(response, "category/categories.html", {"categorysecim": categoryChoose, "posts": posts})

from django.shortcuts import render
from django.views import generic
from .models import PostModel
from .forms import CreateNewPostForm

# Create your views here.
class PostCreateView(generic.CreateView):
    model = PostModel
    # form_class = CreateNewPostForm
    template_name = 'posts/post_create.html'
    # fields = '__all__'
    fields = [
        'title_field',
        'about_field',
        'price_field',
        'currency_field',
        'category_field',
        'sold_or_not_field'
    ]
    
class PostListAllView(generic.ListView):
    model = PostModel
    template_name = 'posts/post_all.html'
    
    
class PostListMineView(generic.ListView):
    model = PostModel
    template_name = 'posts/post_list.html'


class PostDetailsView(generic.DetailView):
    model = PostModel
    template_name = 'posts/post_details.html'
    
    
class PostUpdateView(generic.UpdateView):
    model = PostModel
    template_name = 'posts/post_update.html'
    fields = [
        'title_field',
        'about_field',
        'price_field',
        'currency_field',
        'category_field',
        'sold_or_not_field'
    ]
    
class PostDeleteView(generic.DeleteView):
    pass
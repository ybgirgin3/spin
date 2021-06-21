from django.shortcuts import render, HttpResponseRedirect
from .models import PostModel
from .forms import CreateNewPostForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy
# Create your views here.

# oluşturduktan sonra detaylar sayfasında yönlendirsin
def post_detail_view(response, slug):
    postView = PostModel.objects.get(slug=slug)
    ctx = {
        "post": postView,
    }
    return render(response, "posts/post_details.html" , context=ctx)


def createPostView(response):
    if response.method == 'POST':
        form = CreateNewPostForm(response.POST)
        if form.is_valid():
            title = form.cleaned_data['title_field']
            about = form.cleaned_data['about_field']
            price = form.cleaned_data['price_field']
            currency = form.cleaned_data['currency_field']
            category = form.cleaned_data['category_field']
            p = PostModel(
                title=title,
                about_post=about,
                price=price,
                currency=currency,
                category=category
                )
            response.user.post_user.add(p, bulk=False)
            p.save()
            
            p_slug = PostModel.objects.latest("id")
        return HttpResponseRedirect("/posts/" + p_slug.slug)
    else:
        form = CreateNewPostForm()
    return render(response, "posts/post_create.html", {'form': form})

class update_post_view(UpdateView):
    model = PostModel
    template_name = "posts/post_update.html"
    # fields = "__all__"
    fields = ('title', 'about_post', 'price', 'currency', 'category', 'sold_or_not_model')
    # success_url = reverse_lazy('post_detail_view')


def list_mine_view(response):
    return render(response, "posts/post_list.html")

def list_all_view(response):
    p = PostModel.objects.all()
    return render(response, "posts/post_all.html", {'posts': p})
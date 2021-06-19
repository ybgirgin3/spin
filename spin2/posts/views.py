from django.shortcuts import render, HttpResponseRedirect
from .models import PostModel
from .forms import CreateNewPostForm
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
            title_post = form.cleaned_data['title_field']
            about_post = form.cleaned_data['about_field']
            price_post = form.cleaned_data['price_field']
            p = PostModel(
                title=title_post,
                about_post=about_post,
                price_net=price_post
                )
            # print(dir(response.user))
            response.user.post_user.add(p)
            p.save()
            
            p_slug = PostModel.objects.latest("id")
        return HttpResponseRedirect("/posts" + p_slug.slug)
    else:
        form = CreateNewPostForm()
    return render(response, "posts/post_create.html", {'form': form})

def list_view(response):
    return render(response, "posts/post_list.html")
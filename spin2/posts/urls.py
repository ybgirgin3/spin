from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.createPostView, name="createPostView"),
    path('list-mine/', views.list_mine_view, name="my_posts"),
    path("list-all/", views.list_all_view, name="all_posts"),
    path("posts/<slug:slug>", views.post_detail_view, name="post_detail_view"),
]
from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.createPostView, name="createPostView"),
    path("posts/<slug:slug>", views.post_detail_view, name="post_detail_view"),
]
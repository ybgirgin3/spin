from django.urls import path

from . import views

urlpatterns = [
    path("create/", views.PostCreateView.as_view(), name="createPostView"),
    path('list-mine/', views.PostListMineView.as_view(), name="my_posts"),
    path("list-all/", views.PostListAllView.as_view(), name="all_posts"),
    path("posts/<slug:slug>", views.PostDetailsView.as_view(), name="post_detail_view"),
    path("posts/<slug:slug>/update", views.PostUpdateView.as_view(), name="post_update_view"),
    # path("posts/<slug:slug>/delete", views.update_view, name="post_delete_view")
]
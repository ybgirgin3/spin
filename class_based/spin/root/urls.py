from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("home/", views.HomeView.as_view(), name="home"),
    #path("<int:id>", views.index, name="index"),
    #path("view/", views.view, name="view"),
]
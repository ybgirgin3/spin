from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    #path("<int:id>", views.index, name="index"),
    #path("view/", views.view, name="view"),
]
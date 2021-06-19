from .views import index_view, category_view
from django.urls import path


urlpatterns = [
    path('', index_view, name="index"),
    path('<str:slug>', category_view)
]
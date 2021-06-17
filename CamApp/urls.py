import mymenu
from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path('feed', views.feed, name='feed'),
]
from django.conf.urls import url

import mymenu
from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path('feed', views.feed, name='feed'),
    path('menu_list/', mymenu.views.menu_list, name='menu_list'),

]

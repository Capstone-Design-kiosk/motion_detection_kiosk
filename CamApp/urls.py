from django.conf.urls import url

import mymenu
from . import views
from django.urls import path

urlpatterns = [
    path('index', views.index, name="index"),
    path('feed', views.feed, name='feed'),
    path('', mymenu.views.menu_list, name='menu_list'),

]

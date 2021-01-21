from django.urls import path
from . import views

urlpatterns = [
    path('menu_list/', views.menu_list, name='menu_list'),
    path('menu/<int:menu_id>/', views.menu_detail, name='menu_detail'),
    path('menu/menu_register/', views.menu_register, name='menu_register'),
    path('menu/<int:menu_id>/menu_edit', views.menu_edit, name='menu_edit'),
    path('menu/<int:menu_id>/menu_delete', views.menu_delete, name='menu_delete'),

]


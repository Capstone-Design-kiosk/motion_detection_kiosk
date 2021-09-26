from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('menu_list_coldcoffee/', views.menu_list_coldcoffee, name='menu_list_coldcoffee'),
    path('menu_list_beverage/', views.menu_list_beverage, name='menu_list_beverage'),
    path('menu_list_bake/', views.menu_list_bake, name='menu_list_bake'),
    path('menu/<int:menu_id>/', views.menu_detail, name='menu_detail'),
    path('menu/menu_register/', views.menu_register, name='menu_register'),
    path('menu/<int:menu_id>/menu_edit', views.menu_edit, name='menu_edit'),
    path('menu/<int:menu_id>/menu_delete', views.menu_delete, name='menu_delete'),
    path('menu/<int:list_id>/order_delete', views.order_delete, name='order_delete'),
    path('menu/<int:order_id>/order_confirm', views.order_confirm, name='order_confirm'),
]
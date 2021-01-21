from django.contrib import admin
from .models import Menu, Order, OrderList

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderList)
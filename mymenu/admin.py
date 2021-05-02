from django.contrib import admin
from .models import Menu, Order, OrderList

admin.site.register(Menu)
admin.site.register(Order)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ('list_id', 'order_num', 'menu_num', 'quantity', 'price', 'cup', 'menu_name')
admin.site.register(OrderList,OrderListAdmin)
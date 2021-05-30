from django.contrib import admin
from .models import Menu, Order, OrderList

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'des', 'price', 'cat')
admin.site.register(Menu,MenuAdmin)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ('list_id', 'order_num', 'menu_num', 'quantity', 'price', 'cup', 'menu_name')
admin.site.register(OrderList,OrderListAdmin)
admin.site.register(Order)




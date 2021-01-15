from django.contrib import admin
from .models import Menu, Order, OrderList

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'des', 'price', 'cat')
admin.site.register(Menu,MenuAdmin)
admin.site.register(Order)
admin.site.register(OrderList)



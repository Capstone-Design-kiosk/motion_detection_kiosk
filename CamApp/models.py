from django.db import models
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    image = models.TextField()
    des = models.TextField()
    price = models.CharField(max_length=15)
    cat = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'menu'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    time = models.DateTimeField()
    total_price = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'order'


class OrderList(models.Model):
    list_id = models.AutoField(primary_key=True)
    order_num = models.ForeignKey(Order, models.DO_NOTHING, db_column='order_num')
    menu_num = models.ForeignKey(Menu, related_name='menu_num', on_delete=models.CASCADE, db_column='menu_num')
    menu_name = models.ForeignKey(Menu, to_field='name', related_name='menu_name', on_delete=models.CASCADE, db_column='menu_name')
    quatity = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'order_list'

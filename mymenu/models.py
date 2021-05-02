from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

class Menu(models.Model):
    menu_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(blank=True, upload_to="image", null=True)
    des = models.TextField()
    price = models.CharField(max_length=15)
    cat = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'menu'

class Order(models.Model):
    order_id = models.AutoField(primary_key=True,)
    time = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()

    Myordernum=1  #####주문서번호 (일단은 로그인시 1로설정해놓음 나중에 가장최근값을 가져오도록)

    def auto(ordernum):
     Order.Myordernum=ordernum+1

    class Meta:
        managed = False
        db_table = 'order'


class OrderList(models.Model):
    list_id = models.AutoField(primary_key=True)
    order_num = models.ForeignKey(Order, on_delete=models.DO_NOTHING, db_column='order_num')
    menu_num = models.ForeignKey(Menu, related_name='menu_num', on_delete=models.CASCADE, db_column='menu_num')
    menu_name = models.ForeignKey(Menu,to_field='name', related_name='menu_name', on_delete=models.CASCADE, db_column='menu_name')
    quantity = models.IntegerField(max_length=3)
    price = models.IntegerField(max_length=3)
    cup=models.CharField(max_length=15)
 
    class Meta:
        managed = False
        db_table = 'order_list'


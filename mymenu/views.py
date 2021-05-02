import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

import kiosk
from .models import Menu
from .models import Order
from .models import OrderList
from django.core.paginator import Paginator
from .forms import MenuForm, OrderForm


def menu_list(request):
    Menus = Menu.objects.filter(cat="HOT_COFFEE")
    Myorder=OrderList.objects.filter(order_num=Order.Myordernum) #장바구니 목록 나타냄
    Total = Order.objects.filter(order_id=Order.Myordernum) #최종가격 나타냄
    page = request.GET.get('page', 1)
    paginator = Paginator(Menus, 3) #9로 변경해야함, 일단 확인차
    menu_list = paginator.get_page(page)
    return render(request, 'mymenu/menu_list.html', {"menu_list":menu_list, "Menus":Menus, "Myorder":Myorder,"Total":Total})

def menu_list_coldcoffee(request):
    Menus = Menu.objects.filter(cat="COLD_COFFEE")
    Myorder=OrderList.objects.filter(order_num=Order.Myordernum) #장바구니 목록 나타냄
    Total = Order.objects.filter(order_id=Order.Myordernum) #최종가격 나타냄
    page = request.GET.get('page', 1)
    paginator = Paginator(Menus, 3) #9로 변경해야함, 일단 확인차
    menu_list = paginator.get_page(page)
    return render(request, 'mymenu/menu_list.html', {"menu_list":menu_list, "Menus":Menus, "Myorder":Myorder,"Total":Total})

def menu_list_beverage(request):
    Menus = Menu.objects.filter(cat="BEVERAGE")
    Myorder=OrderList.objects.filter(order_num=Order.Myordernum) #장바구니 목록 나타냄
    Total = Order.objects.filter(order_id=Order.Myordernum) #최종가격 나타냄
    page = request.GET.get('page', 1)
    paginator = Paginator(Menus, 3) #9로 변경해야함, 일단 확인차
    menu_list = paginator.get_page(page)
    return render(request, 'mymenu/menu_list.html', {"menu_list":menu_list, "Menus":Menus, "Myorder":Myorder,"Total":Total})

def menu_list_bake(request):
    Menus = Menu.objects.filter(cat="BAKE")
    Myorder=OrderList.objects.filter(order_num=Order.Myordernum) #장바구니 목록 나타냄
    Total = Order.objects.filter(order_id=Order.Myordernum) #최종가격 나타냄
    page = request.GET.get('page', 1)
    paginator = Paginator(Menus, 3) #9로 변경해야함, 일단 확인차
    menu_list = paginator.get_page(page)
    return render(request, 'mymenu/menu_list.html', {"menu_list":menu_list, "Menus":Menus, "Myorder":Myorder,"Total":Total})


def menu_register(request):
    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.save()
            return redirect('menu_detail', menu_id=menu.pk)
    else:
        form = MenuForm()
    return render(request, 'mymenu/menu_register.html', {'form':form})


def menu_delete(request, menu_id):
    menu = get_object_or_404(Menu, pk=menu_id)
    menu.delete()
    return redirect('mymenu/menu_list/',{"menu_list":menu_list})

def menu_edit(request, menu_id):
    menu=get_object_or_404(Menu, pk=menu_id)
    if request.method=="POST":
        form=MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu=form.save(commit=False)
            menu.save()
            return redirect('menu_detail',menu_id=menu.pk)
    else:
        form=MenuForm(instance=menu)
    return render(request,'mymenu/menu_edit.html',{'form':form})

def menu_detail(request,menu_id):  #주문서 페이지 들어가기
    menu_detail=get_object_or_404(Menu, pk=menu_id)
    w1=Order(order_id=Order.Myordernum,time=datetime.datetime.now()) #DB order 생성
    w1.save()
    if request.method == "POST":  #주문페이지
        menu_id=Menu.objects.get(menu_id=request.POST['menu_id'])
        name=Menu.objects.get(name=request.POST['name'])
        order_id = Order.objects.get(order_id=Order.Myordernum)
        price= request.POST['price']
        quantity = request.POST['quantity']
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.menu_num=menu_id
            order.menu_name=name
            order.order_num=order_id
            order.price=int(price)*int(quantity)
            order.save()
            now = datetime.datetime.now()
            Order.objects.filter(order_id=Order.Myordernum).update(time=now)
            sum = OrderList.objects.filter(order_num=Order.Myordernum).aggregate(Sum('price'))
            Order.objects.filter(order_id=Order.Myordernum).update(total_price=sum['price__sum'])
           
            return redirect('menu_list')
    else:
        form = OrderForm()
    return render(request, 'mymenu/menu_detail.html',{'menu':menu_detail,'form':form,})

def order_confirm(request,order_id):
    if order_id == Order.Myordernum:
        Order.auto(order_id)
    return redirect('/mymenu/menu_list/',{"menu_list":menu_list})
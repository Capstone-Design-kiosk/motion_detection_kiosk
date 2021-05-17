import datetime

from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404

import kiosk
from .models import Menu
from .models import Order
from .models import OrderList
from django.core.paginator import Paginator
from .forms import MenuForm, OrderForm
trynum=0#프로그램 실행시 처음 사용자인지 여부 확인용
try:
    latestnum = OrderList.objects.latest('order_num')#가장 최신 주문번호
    latestnum2=hash(latestnum.order_num)+1
except OrderList.DoesNotExist:#맨처음 프로그램 실행시 order내용이 아예 없을 때
    latestnum2=1

newnum=latestnum2+1#결제하기 누르고 다음 사람을 위해 이어지는 주문번호

def menu_list(request):
    if trynum==0:#########################################프로그램 처음 실행시 가장 최신 번호(당일 첫사용자)
        Menus = Menu.objects.filter(cat="HOT_COFFEE")
        Myorder = OrderList.objects.filter(order_num=latestnum2)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=latestnum2)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3) #9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html', {"menu_list":menu_list, "Menus":Menus, "Myorder":Myorder,"Total":Total})
    else:#########################################결제하기 누른 이후 최신번호+1의 번호로 갱신되어 newnum사용(당일 두전째 사용자부터 그 이후)
        Menus = Menu.objects.filter(cat="HOT_COFFEE")
        Myorder = OrderList.objects.filter(
            order_num=newnum)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=newnum)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3)  # 9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html',
                      {"menu_list": menu_list, "Menus": Menus, "Myorder": Myorder, "Total": Total})
def menu_list_coldcoffee(request):
    if trynum == 0:  #########################################프로그램 처음 실행시 가장 최신 번호(당일 첫사용자)
        Menus = Menu.objects.filter(cat="COLD_COFFEE")
        Myorder = OrderList.objects.filter(order_num=latestnum2)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=latestnum2)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3)  # 9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html',
                      {"menu_list": menu_list, "Menus": Menus, "Myorder": Myorder, "Total": Total})
    else:  #########################################결제하기 누른 이후 최신번호+1의 번호로 갱신되어 newnum사용(당일 두전째 사용자부터 그 이후)
        Menus = Menu.objects.filter(cat="COLD_COFFEE")
        Myorder = OrderList.objects.filter(
            order_num=newnum)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=newnum)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3)  # 9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html',
                      {"menu_list": menu_list, "Menus": Menus, "Myorder": Myorder, "Total": Total})
def menu_list_beverage(request):
    if trynum == 0:  #########################################프로그램 처음 실행시 가장 최신 번호(당일 첫사용자)
        Menus = Menu.objects.filter(cat="BEVERAGE")
        Myorder = OrderList.objects.filter(order_num=latestnum2)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=latestnum2)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3)  # 9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html',
                      {"menu_list": menu_list, "Menus": Menus, "Myorder": Myorder, "Total": Total})
    else:  #########################################결제하기 누른 이후 최신번호+1의 번호로 갱신되어 newnum사용(당일 두전째 사용자부터 그 이후)
        Menus = Menu.objects.filter(cat="BEVERAGE")
        Myorder = OrderList.objects.filter(
            order_num=newnum)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=newnum)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3)  # 9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html',
                      {"menu_list": menu_list, "Menus": Menus, "Myorder": Myorder, "Total": Total})
def menu_list_bake(request):
    if trynum == 0:  #########################################프로그램 처음 실행시 가장 최신 번호(당일 첫사용자)
        Menus = Menu.objects.filter(cat="BAKE")
        Myorder = OrderList.objects.filter(order_num=latestnum2)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=latestnum2)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3)  # 9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html',
                      {"menu_list": menu_list, "Menus": Menus, "Myorder": Myorder, "Total": Total})
    else:  #########################################결제하기 누른 이후 최신번호+1의 번호로 갱신되어 newnum사용(당일 두전째 사용자부터 그 이후)
        Menus = Menu.objects.filter(cat="BAKE")
        Myorder = OrderList.objects.filter(
            order_num=newnum)  # 장바구니 목록 나타냄(hash:object객체의 int값 반환)
        Total = Order.objects.filter(order_id=newnum)  # 최종가격 나타냄
        page = request.GET.get('page', 1)
        paginator = Paginator(Menus, 3)  # 9로 변경해야함, 일단 확인차
        menu_list = paginator.get_page(page)
        return render(request, 'mymenu/menu_list.html',
                      {"menu_list": menu_list, "Menus": Menus, "Myorder": Myorder, "Total": Total})

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
    w1=Order(order_id=latestnum2,time=datetime.datetime.now()) #DB order 생성
    w1.save()
    if trynum == 0:
        if request.method == "POST":  #주문페이지
            menu_id=Menu.objects.get(menu_id=request.POST['menu_id'])
            name = Menu.objects.get(name=request.POST['name'])  # 제품이름 표시
            order_id = Order.objects.get(order_id=latestnum2)
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
                Order.objects.filter(order_id=latestnum2).update(time=now)
                sum = OrderList.objects.filter(order_num=latestnum2).aggregate(Sum('price'))
                Order.objects.filter(order_id=latestnum2).update(total_price=sum['price__sum'])

                return redirect('menu_list')
        else:
            form = OrderForm()
    else:
        if request.method == "POST":  # 주문페이지
            menu_id = Menu.objects.get(menu_id=request.POST['menu_id'])
            name = Menu.objects.get(name=request.POST['name'])  # 제품이름 표시
            order_id = Order.objects.get(order_id=newnum)
            price = request.POST['price']
            quantity = request.POST['quantity']
            form = OrderForm(request.POST, request.FILES)
            if form.is_valid():
                order = form.save(commit=False)
                order.menu_num = menu_id
                order.menu_name = name
                order.order_num = order_id
                order.price = int(price) * int(quantity)
                order.save()
                now = datetime.datetime.now()
                Order.objects.filter(order_id=newnum).update(time=now)
                sum = OrderList.objects.filter(order_num=newnum).aggregate(Sum('price'))
                Order.objects.filter(order_id=newnum).update(total_price=sum['price__sum'])

                return redirect('menu_list')
        else:
            form = OrderForm()
    return render(request, 'mymenu/menu_detail.html',{'menu':menu_detail,'form':form,})

def order_confirm(request, order_id):
    if order_id == latestnum2:
        global trynum
        trynum+=1 #trynum은 프로그램 실행시 처음 사용자인지 여부 구별용도
    return redirect('/mymenu/menu_list/',{"menu_list":menu_list})
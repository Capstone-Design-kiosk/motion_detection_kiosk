from datetime import timezone

from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu
from django.core.paginator import Paginator


def menu_list(request):
    Menus = Menu.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(Menus, 3) #9로 변경해야함, 일단 확인차
    menu_list = paginator.get_page(page)
    return render(request, 'menu/menu_list.html', {"menu_list":menu_list ,'Menus':Menus})

def postcreate(request): #메뉴 등록
    blog = Menu()
    blog.name = request.POST['name']
    blog.des = request.POST['des']
    blog.image = request.FILES['image']
    blog.price=request.POST['price']
    blog.cat=request.POST['cat']
    blog.save()
    return redirect('/menu_list/')

def menu_register(request):
    return render(request, 'menu/menu_register.html')


def menu_delete(request, menu_id):
    menu= get_object_or_404(Menu, pk=menu_id)
    menu.delete()
    return redirect('/menu_list/')


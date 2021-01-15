from datetime import timezone

from django.shortcuts import render, redirect
from .models import Menu

def menu_list(request):
    Menus = Menu.objects.all()
    return render(request, 'menu/menu_list.html',{"Menus":Menus})

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
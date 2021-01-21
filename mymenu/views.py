from datetime import timezone
from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu
from django.core.paginator import Paginator
from .forms import MenuForm

def menu_list(request):
    Menus = Menu.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(Menus, 3) #9로 변경해야함, 일단 확인차
    menu_list = paginator.get_page(page)
    return render(request, 'mymenu/menu_list.html', {"menu_list":menu_list,'Menus':Menus})

def menu_detail(request,menu_id):
    menu_detail=get_object_or_404(Menu, pk=menu_id)
    return render(request, 'mymenu/menu_detail.html',{'menu':menu_detail,})

def menu_register(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
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
    return redirect('/menu_list/')

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
from django import forms
from .models import Menu, OrderList

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = {'name', 'image', 'des', 'price', 'cat',}

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderList
        fields = {'quantity','cup',}


        widgets = {
            #포장 여부는 checkbox
        }
        labels = {
            'quantity': '수량',
            'cup': '포장여부',
        }
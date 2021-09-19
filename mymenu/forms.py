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
        # CUP_CHOICES = (
        #     ('', '포장 여부 선택'),
        #     ('HERE', 'HERE'),  # First one is the value of select option and second is the displayed value in option
        #     ('TOGO', 'TOGO'),
        # )
        # widgets = {
        #     'cup': forms.CheckboxSelectMultiple,
        # }
        labels = {
            'quantity': '수량',
            'cup': '포장여부',
        }
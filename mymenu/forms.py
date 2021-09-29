from django import forms
from django.forms.widgets import NumberInput
from .models import Menu, OrderList


# from ckeditor_uploader.widgets import CKEditorUploadingWidget

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = {'name', 'image', 'des', 'price', 'cat', }


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderList
        fields = {'quantity', 'cup', }
        # q_num = [(q_num, q_num) for q_num in range(1, 50)]
        # CUP_CHOICES = (
        #     ('', '포장 여부 선택'),
        #     ('HERE', 'HERE'),  # First one is the value of select option and second is the displayed value in option
        #     ('TOGO', 'TOGO'),
        # )
        # widgets = {
        #     'quantity': forms.Select(choices=q_num)
        # }
        # widget=NumberInput(attrs={'type':'range', 'step': '2'})

        labels = {
            'quantity': '수량',
            'cup': '포장여부',
        }
from django import forms
from Foodplazaapp.models import Food,Customer,Cart,Admin,Orders

class FoodForm(forms.ModelForm):
    class Meta:
        model=Food
        fields="__all__"

class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"

class AdminForm(forms.ModelForm):
    class Meta:
        model=Admin
        fields="__all__"

class CartForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields="__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields="__all__"
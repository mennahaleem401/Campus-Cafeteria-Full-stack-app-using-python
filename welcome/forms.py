
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category', 'image', 'is_available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input'}),
            'price': forms.NumberInput(attrs={'class': 'form-input', 'step': '0.01'}),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'image': forms.TextInput(attrs={'class': 'form-input', 'placeholder': '🍕'}),
        }
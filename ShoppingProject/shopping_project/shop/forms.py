from django import forms
from .models import Product

class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'description', 'price', 'available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ProductForm:
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']  # 根据您的模型字段调整
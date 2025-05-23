from django import forms
from .models import Product

class ProductUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'image', 'description', 'price', 'available']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category']  # 根据您的模型字段调整

    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            raise forms.ValidationError("商品slug不可为空")
        return slug
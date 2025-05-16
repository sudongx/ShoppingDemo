from django.shortcuts import render, get_object_or_404,redirect
from .models import Category, Product
from .forms import ProductUploadForm
from django.contrib import messages
from .forms import ProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'shop/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product_detail.html', {'product': product})


def contact(request):
    return render(request, 'shop/contact.html', {'title': '联系我们'})


def about(request):
    return render(request, 'shop/about.html', {'title': '关于我们'})


def upload_product(request):
    if request.method == 'POST':
        form = ProductUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '商品上传成功！')
            return redirect('shop:product_list')
    else:
        form = ProductUploadForm()
    return render(request, 'shop/upload_product.html', {'form': form})

def faq(request):
    return render(request, 'shop/faq.html', {'title': '常见问题'})

def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')  # 上传成功后重定向到商品列表
    else:
        form = ProductForm()
    return render(request, 'shop/upload_product.html', {'form': form})
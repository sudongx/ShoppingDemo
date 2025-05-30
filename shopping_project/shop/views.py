from django.shortcuts import render, get_object_or_404,redirect
from .forms import ProductUploadForm
from django.contrib import messages
from .forms import ProductForm
from django.shortcuts import get_object_or_404
from .models import Product, Category
from .models import Product, Cart, CartItem
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session


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


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product, id=id, slug=product_slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})


def contact(request):
    return render(request, 'shop/contact.html')


def contact_submit(request):
    if request.method == 'POST':
        # 处理表单数据
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # 这里可以添加邮件发送逻辑或保存到数据库
        # 例如：send_mail(subject, message, email, ['admin@example.com'])

        messages.success(request, '感谢您的留言，我们会尽快回复！')
        return redirect('shop:contact')  # 重定向到联系页面

    # 如果不是POST请求，重定向到联系页面
    return redirect('shop:contact')


def about(request):
    return render(request, 'shop/about.html', {'title': '关于我们'})


def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # 使用 ProductForm
        if form.is_valid():
            form.save()
            messages.success(request, '商品上传成功！')
            return redirect('shop:product_list')
    else:
        form = ProductForm()  # 使用 ProductForm
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

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'price': product.price}
    )
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('shop:product_list')  # 重定向到商品列表或购物车页面

@login_required
def cart_detail(request):
    cart = request.user.cart
    return render(request, 'shop/cart_detail.html', {'cart': cart})

def simulate_payment(request):
    cart = get_or_create_cart(request)
    if request.method == 'POST':
        # 模拟支付逻辑（记录订单、清空购物车）
        # 此处可添加订单生成逻辑
        cart.items.all().delete()
        return render(request, 'shop/payment_success.html')
    return render(request, 'shop/payment.html', {'cart': cart})


def get_or_create_cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.save()  # 生成新会话
        session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(session__session_key=session_key)
    # 清理过期会话的购物车
    if created or not cart.session.is_valid():
        cart.session = Session.objects.get(session_key=session_key)
        cart.save()
    return cart


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)
    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'price': product.price}
    )
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    # 重定向到购物车或商品详情页
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def cart_detail(request):
    cart = get_or_create_cart(request)
    return render(request, 'shop/cart_detail.html', {'cart': cart})
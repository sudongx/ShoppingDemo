from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from .models import Product, Category, Cart, CartItem
from .forms import ProductForm, ProductUploadForm
from django.contrib.auth.forms import UserCreationForm

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
    product = get_object_or_404(Product, id=id, slug=product_slug)

    # 如果商品没有图片，设置一个默认图片路径
    if not product.image:
        product.image = '/static/images/default-product.jpg'  # 确保静态目录中有此图片

    return render(request, 'shop/product_detail.html', {'product': product})

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
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '商品上传成功！')
            return redirect('shop:product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/upload_product.html', {'form': form})


def faq(request):
    return render(request, 'shop/faq.html', {'title': '常见问题'})


def get_or_create_cart(request):
    """获取或创建用户购物车，支持匿名用户"""
    # 如果用户已登录，使用用户关联的购物车
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return cart

    # 匿名用户使用基于会话的购物车
    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = get_or_create_cart(request)

    # 对于匿名用户，使用会话存储购物车
    if not request.user.is_authenticated:
        # 实现匿名购物车逻辑
        cart_id = request.session.get('cart_id')
        if not cart_id:
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
        else:
            try:
                cart = Cart.objects.get(id=cart_id)
            except Cart.DoesNotExist:
                cart = Cart.objects.create()
                request.session['cart_id'] = cart.id
    else:
        # 已登录用户，使用用户关联的购物车
        cart, created = Cart.objects.get_or_create(user=request.user)
    # 检查商品库存
    if product.stock <= 0:
        messages.error(request, '该商品已售罄！')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    cart_item, item_created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'price': product.price, 'quantity': 1}
    )

    if not item_created:
        # 检查库存是否足够
        if cart_item.quantity + 1 > product.stock:
            messages.error(request, f'该商品库存不足，最多只能购买{product.stock}件！')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, f'已将"{product.name}"添加到购物车！')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)
    cart_item.delete()
    messages.success(request, '已从购物车移除该商品！')
    return redirect('shop:cart_detail')


@login_required
def update_cart(request, item_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user)

        # 检查库存
        if quantity > cart_item.product.stock:
            messages.error(request, f'该商品库存不足，最多只能购买{cart_item.product.stock}件！')
            quantity = cart_item.product.stock

        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('shop:cart_detail')


@login_required
def cart_detail(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()

    # 计算总价
    total_price = sum(item.subtotal() for item in cart_items)

    return render(request, 'shop/cart_detail.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price
    })


@login_required
def simulate_payment(request):
    cart = get_or_create_cart(request)
    cart_items = cart.items.all()

    if not cart_items:
        messages.error(request, '购物车为空，无法结算！')
        return redirect('shop:cart_detail')

    if request.method == 'POST':
        # 模拟支付逻辑
        # 1. 创建订单
        # 2. 扣减库存
        # 3. 清空购物车

        # 示例代码，实际项目需要完善订单系统
        for item in cart_items:
            item.product.stock -= item.quantity
            item.product.save()

        cart_items.delete()
        messages.success(request, '支付成功！订单已生成。')
        return redirect('shop:payment_success')

    return render(request, 'shop/payment.html', {'cart': cart})


def payment_success(request):
    return render(request, 'shop/payment_success.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:login')  # 重定向到登录页面
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def delete_product(request, product_id):
    # 验证用户是否为管理员
    if not request.user.is_staff:
        return redirect('shop:product_list')

    # 获取要删除的商品
    product = get_object_or_404(Product, id=product_id)

    # 处理 POST 请求（确认删除）
    if request.method == 'POST':
        product.delete()
        return redirect('shop:product_list')  # 重定向到商品列表页

    # 渲染确认页面（GET 请求）
    return render(request, 'shop/product_confirm_delete.html', {'product': product})

def edit_product(request, product_id):
    # 权限检查
    if not request.user.is_staff:
        return redirect('shop:product_list')

    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('shop:product_detail', id=product.id, product_slug=product.slug)
    else:
        form = ProductForm(instance=product)

    return render(request, 'shop/product_edit.html', {
        'form': form,
        'product': product
    })
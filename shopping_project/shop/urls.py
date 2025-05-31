from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'shop'

urlpatterns = [
    # 主页和分类页
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),

    # 管理页面
    path('manage/product/<int:product_id>/edit/', views.edit_product, name='edit_product'),
    path('manage/product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('manage/upload-product/', views.upload_product, name='upload_product'),  # 移至管理组

    # 商品详情
    path('product/<int:id>/<slug:product_slug>/', views.product_detail, name='product_detail'),

    # 页面导航
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
    path('faq/', views.faq, name='faq'),

    # 购物车功能
    path('cart/add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('cart/detail/', views.cart_detail, name='cart_detail'),
    path('cart/', views.cart_detail, name='cart_summary'),  # 重定向到详情页

    # 支付功能
    path('pay/', views.simulate_payment, name='simulate_payment'),

    # 用户账户
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),
]
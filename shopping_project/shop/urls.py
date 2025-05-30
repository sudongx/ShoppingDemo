from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('category/<slug:category_slug>/',
         views.product_list,
         name='product_list_by_category'),  # 按分类筛选商品
    path('about/', views.about, name='about'),
    path('category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    # 添加商品详情页路径
    path('product/<int:id>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('upload/', views.upload_product, name='upload_product'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('pay/', views.simulate_payment, name='simulate_payment'),
    path('contact/submit/', views.contact_submit, name='contact_submit'),
]
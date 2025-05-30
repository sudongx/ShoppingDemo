from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from slugify import slugify
from unidecode import unidecode
from django.contrib.auth.models import User
from decimal import Decimal
from django.contrib.sessions.models import Session

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = '分类'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True,blank=False, null=False)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stock = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    class Meta:
        ordering = ('-created',)
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

@receiver(pre_save, sender=Product)
def product_pre_save(sender, instance, **kwargs):
    if not instance.slug:
        # 先将中文转为拼音，再生成slug
        chinese_to_pinyin = unidecode(instance.name)
        instance.slug = slugify(chinese_to_pinyin)

#加入购物车和模拟支付
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return f"Cart for {self.user.username}"

    def get_total_price(self):
        total = 0
        for item in self.cart_items.all():
            total += item.get_total_price()
        return total

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='cart_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name} in cart for {self.cart.user.username}"

    def get_total_price(self):
        return self.product.price * self.quantity
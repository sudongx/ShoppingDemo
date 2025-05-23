from django.db import migrations
from django.utils.text import slugify
from unidecode import unidecode  # 确保已安装

DEFAULT_CATEGORIES = [
    "食品", "饮料", "日用品", "家居用品", "服装", "鞋包",
    "电子产品", "美妆护肤", "母婴用品", "图书音像", "生鲜水果"
]

def add_initial_categories(apps, schema_editor):
    Category = apps.get_model('shop', 'Category')
    for name in DEFAULT_CATEGORIES:
        # 手动生成唯一slug（例如："食品" → "shi-pin"）
        pinyin_name = unidecode(name)
        slug = slugify(pinyin_name)
        Category.objects.create(name=name, slug=slug)

def remove_initial_categories(apps, schema_editor):
    Category = apps.get_model('shop', 'Category')
    Category.objects.filter(name__in=DEFAULT_CATEGORIES).delete()

class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0001_initial'),  # 确保依赖模型创建的迁移
    ]

    operations = [
        migrations.RunPython(add_initial_categories, remove_initial_categories),
    ]
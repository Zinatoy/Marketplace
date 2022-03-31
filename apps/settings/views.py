from unicodedata import category
from django.shortcuts import render
from apps.settings.models import Setting
from apps.products.models import Product
from apps.categories.models import Category

# Create your views here.
def index(request):
    home = Setting.objects.latest('id')
    slide_products = Product.objects.all().order_by('-id')[:5]
    products = Product.objects.all().order_by('-id')[:8]
    one_random_product = Product.objects.all().order_by('?')[:1]
    two_random_product = Product.objects.all().order_by('?')[:1]
    three_random_product = Product.objects.all().order_by('?')[:1]
    expensive_products = Product.objects.all().order_by('-price')[:3]
    categories = Category.objects.all().order_by('-id')
    context = {
        'home' : home,
        'products' : products,
        'slide_products' : slide_products,
        'one_random_product' : one_random_product,
        'two_random_product' : two_random_product,
        'three_random_product' : three_random_product,
        'expensive_products' : expensive_products,
        'categories' : categories
    }
    return render(request, 'index-2.html', context)
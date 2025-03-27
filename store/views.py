from django.shortcuts import render,get_object_or_404
from .models import Product
from category.models import Category
# Create your views here.

def store(request, category_slugs=None):
    categories = None
    products   = None
    if category_slugs !=None:
        categories = get_object_or_404(Category, slug=category_slugs)
        products = Product.objects.all().filter(category=categories,is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available = True)
        product_count = products.count()
    context = {
        'products' : products,
        'product_count' : product_count,
    }
    return render(request,'store/store.html',context)
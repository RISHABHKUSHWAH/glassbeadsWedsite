from django.shortcuts import render
from store.models import Product

def index(request):
    products = Product.objects.all().filter(is_available = True)
    context = {
        'products': products,
    }
    for i in products:
        print(i.images.url)
    return render(request,'index.html',context)
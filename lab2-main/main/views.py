from django.shortcuts import render
from .models import Product, Tag



def index(request):
    return render(request, 'index.html')

def shop(request):
    products = Product.objects.all()
    
    context = {
        'products': products
    }
    return render(request, "shop.html", context)

def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def blog(request):
    products = Product.objects.all()
    # tags = Tag.objects.all()
    context = {
        'products': products,
        # 'tags': tags
    }
    return render(request, "blog.html", context)

def contact(request):
    return render(request, "contact.html")

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def thankyou(request):
    return render(request, "thankyou.html")

def test(request):
    data = ''
    if request.method=="GET":
        data = request.GET['soz']
    context = {
        'data': data
    }
    
    return render(request, "test.html", context)


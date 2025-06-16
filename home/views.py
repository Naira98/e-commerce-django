from django.shortcuts import render
from products.models import Product


def home(request):
    print("IN HOME VIEW")
    # new_products = Product.objects.order_by('-created_at')[:6]
    new_products = Product.objects.all()[:3]

    return render(request, "home/home.html", {"new_products": new_products})


def about(request):
    return render(request, "home/about.html")


def contact(request):
    return render(request, "home/contact.html")

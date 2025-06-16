from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.all()
    return render(
        request,
        "products/products.html",
        {
            "products": products,
            "categories": [{"id": 1, "name": "Clothings"}, {"id": 2, "name": "Shoes"}],
        },
    )


def products_by_category(request, category):
    products = Product.objects.all()
    return render(
        request,
        "products/products.html",
        {
            "products": products,
            "categories": [{"id": 1, "name": "Clothings"}, {"id": 2, "name": "Shoes"}],
        },
    )

def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "products/product_details.html", {"product": product})

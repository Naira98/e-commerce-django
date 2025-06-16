from django.shortcuts import render
from .models import Product, Category


def products(request):
    return render(
        request,
        "products/products.html",
        {
            "products": Product.objects.all(),
            "categories": Category.objects.all(),
        },
    )


def products_by_category(request, category_id):
    return render(
        request,
        "products/products.html",
        {
            "products": Product.objects.filter(category=category_id),
            "categories": Category.objects.all(),
        },
    )


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "products/product_details.html", {"product": product})

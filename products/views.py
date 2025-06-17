from django.shortcuts import render
from .models import Product, Category
import math


def products(request):
    category_id = request.GET.get("category")
    try:
        category_id = int(category_id) if category_id else None
    except (TypeError, ValueError):
        category_id = None

    try:
        page_number = int(request.GET.get("page", 1))
    except (TypeError, ValueError):
        page_number = 1

    per_page_options = [3, 6, 9]
    try:
        per_page = int(request.GET.get("per_page", 6))
        if per_page not in per_page_options:
            per_page = 6
    except (TypeError, ValueError):
        per_page = 6

    categories = Category.objects.all()
    filtered_products = (
        Product.objects.filter(categories__id=category_id)
        if category_id
        else Product.objects.all()
    )

    total_products = filtered_products.count()
    number_of_pages = math.ceil(total_products / per_page) if per_page else 1
    start = per_page * (page_number - 1)
    end = start + per_page
    products = filtered_products[start:end]

    context = {
        "products": products,
        "categories": categories,
        "selected_category": category_id,
        "per_page": per_page,
        "per_page_options": per_page_options,
        "number_of_pages": range(1, number_of_pages + 1),
        "page_number": page_number
    }
    return render(request, "products/products.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "products/product_details.html", {"product": product})

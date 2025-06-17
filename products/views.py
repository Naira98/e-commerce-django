from django.shortcuts import render
from .models import Product, Category


def products(request):
    try:
        category_id = request.GET.get("category")
        category_id = int(category_id) if category_id else None
    except ValueError:
        category_id = None

    try:
        page_number = int(request.GET.get("page")) 
    except:
        page_number = 1

    per_page_options = [3, 6, 9]
    try:
        per_page = int(request.GET.get("per_page")) 
        if per_page not in per_page_options:
            per_page = 6
    except:
        per_page = 6


    categories = Category.objects.all()

    if category_id:
        products = Product.objects.filter(categories__id=category_id)
    else:
        products = Product.objects.all()


    context = {
        "products": products[per_page * (page_number - 1) : page_number * per_page],
        "categories": categories,
        "selected_category": category_id,
        "per_page": per_page,
        "per_page_options": per_page_options,
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "products/product_details.html", {"product": product})

from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from .forms import ProductForm

# List Products
def admin_dashboard(request):
    products = Product.objects.all()
    return render(request, "dashboard/dashboard.html", {"products": products})


# Create New Product
def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = ProductForm()
    return render(
        request, "dashboard/product_form.html", {"form": form, "title": "Create Product"}
    )


# Edit Product
def product_edit(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect("admin_dashboard")
    else:
        form = ProductForm(instance=product)
    return render(
        request, "dashboard/product_form.html", {"form": form, "title": "Edit Product"}
    )


# Delete Product
def product_delete(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect("admin_dashboard")

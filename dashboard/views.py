from django.views.generic import ListView, CreateView, UpdateView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from products.models import Product
from .forms import ProductForm

class AdminProductListView(ListView):
    model = Product
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'products'


class AdminProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/product_form.html'
    success_url = reverse_lazy('admin_dashboard')


class AdminProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/product_form.html'
    success_url = reverse_lazy('admin_dashboard')


class AdminProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return redirect(reverse_lazy('admin_dashboard'))

from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from products.models import Product, Category
from .forms import ProductForm, CategoryForm

@method_decorator(staff_member_required, name='dispatch')
class AdminProductListView(ListView):
    model = Product
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.all().order_by('id') 


@method_decorator(staff_member_required, name='dispatch')
class AdminProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/product_form.html'
    success_url = reverse_lazy('admin_dashboard')

@method_decorator(staff_member_required, name='dispatch')
class AdminProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'dashboard/product_form.html'
    success_url = reverse_lazy('admin_dashboard')

@method_decorator(staff_member_required, name='dispatch')
class AdminProductDeleteView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        product.delete()
        return redirect(reverse_lazy('admin_dashboard'))
    
@method_decorator(staff_member_required, name='dispatch')   
class AdminCategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'dashboard/category_from.html'
    success_url = reverse_lazy('admin_dashboard')

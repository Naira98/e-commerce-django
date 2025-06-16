from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdminProductListView.as_view(), name='admin_dashboard'),
    path('products/new/', views.AdminProductCreateView.as_view(), name='admin_product_create'),
    path('products/<int:pk>/edit/', views.AdminProductUpdateView.as_view(), name='admin_product_edit'),
    path('products/<int:pk>/delete/', views.AdminProductDeleteView.as_view(), name='admin_product_delete'),
]
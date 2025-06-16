from django.urls import path

from . import views

APP_NAME="products"
urlpatterns = [
    path('', views.admin_dashboard, name='admin_dashboard'),
    path('products/new/', views.product_create, name='admin_product_create'),
    path('products/<int:product_id>/edit/', views.product_edit, name='admin_product_edit'),
    path('products/<int:product_id>/delete/', views.product_delete, name='admin_product_delete'),
]

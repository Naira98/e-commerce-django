from django.urls import path

from . import views

urlpatterns = [
    path("", views.products, name="products"),
    path("category/<str:category>", views.products_by_category, name="products_by_category"), 
    path("details/<int:product_id>", views.product_details, name="product_details"),
]

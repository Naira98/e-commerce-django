from django.db import models
from django.core.exceptions import ValidationError


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    categories = models.ManyToManyField(
        Category, related_name="products", blank=False
    )
    available_stock = models.PositiveIntegerField(null=False, blank=False)
    image = models.ImageField(upload_to="product_images/", null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    def clean(self):
        super().clean()
        if self.price <= 0:
            raise ValidationError({"price": "Price must be a positive value."})

    def __str__(self):
        return self.name

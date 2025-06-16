from django.db import models
from django.core.exceptions import ValidationError
import datetime


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name="products",
    )
    available_stock = models.PositiveIntegerField(null=False, blank=False, default=1)
    image = models.ImageField(upload_to="product_images/", null=False, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False, blank=False)

    def clean(self):
        super().clean()
        if self.price <= 0:
            raise ValidationError({"price": "Price must be a positive value."})

    def __str__(self):
        return self.name

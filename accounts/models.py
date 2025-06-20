from django.contrib.auth.models import AbstractUser
from django.db import models

from products.models import Product


class CustomUser(AbstractUser):
    profile_picture = models.ImageField(
        upload_to="product_images/", null=True, blank=True
    )
    favorites = models.ManyToManyField(Product, related_name="favorited_by", blank=True)

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available_stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return self.name

from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


# class Size(models.Model):
#     name = models.CharField(max_length=10, unique=True)



# class Color(models.Model):
#     name = models.CharField(max_length=20, unique=True)



class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    # sizes = models.ManyToManyField(Size)
    # colors = models.ManyToManyField(Color)
    available_stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="product_images/")

    def __str__(self):
        return self.name

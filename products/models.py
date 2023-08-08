import os.path
import uuid

from django.db import models
from django.utils.text import slugify

from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    # class Meta:
    #     ordering = ["name"]

    def __str__(self) -> str:
        return self.name


def product_image_file_path(instance, filename) -> str:
    _, extension = os.path.splitext(filename)

    return os.path.join(
        "uploads", "products",
        f"{slugify(instance.name)}-{uuid.uuid4()}{extension}"
    )


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=product_image_file_path)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    # class Meta:
    #     ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} added {self.product.name}, {self.product.price}"



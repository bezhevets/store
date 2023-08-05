from django.urls import path

from products.views import index, products

urlpatterns = [
    path("", index, name="index"),
    path("products/", products, name="products"),
]


app_name = "products"

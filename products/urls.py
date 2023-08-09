from django.urls import path

from products.views import index, products, basket_add, basket_remove

urlpatterns = [
    path("", index, name="index"),
    path("products/", products, name="products"),
    path("category/<int:category_id>", products, name="category"),
    path("basket/add/<int:pk>", basket_add, name="basket_add"),
    path("basket/remove/<int:pk>", basket_remove, name="basket_remove"),
]


app_name = "products"

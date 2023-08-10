from django.urls import path

from products.views import products, basket_add, basket_remove, IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/", products, name="products"),
    path("category/<int:category_id>", products, name="category"),
    path("page/<int:page_num>", products, name="paginator"),
    path("basket/add/<int:pk>", basket_add, name="basket_add"),
    path("basket/remove/<int:pk>", basket_remove, name="basket_remove"),
]


app_name = "products"

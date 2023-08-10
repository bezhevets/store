from django.urls import path

from products.views import basket_add, basket_remove, IndexView, ProductsListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("products/", ProductsListView.as_view(), name="products"),
    path("category/<int:category_id>", ProductsListView.as_view(), name="category"),
    path("page/<int:page>", ProductsListView.as_view(), name="paginator"),
    path("basket/add/<int:pk>", basket_add, name="basket_add"),
    path("basket/remove/<int:pk>", basket_remove, name="basket_remove"),
]


app_name = "products"

from django.contrib import admin

from products.models import Product, ProductCategory


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity", "category"]
    list_filter = ["category"]
    search_fields = ["name"]

admin.site.register(ProductCategory)

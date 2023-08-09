from django.contrib import admin

from products.models import Product, ProductCategory, Basket


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "quantity", "category"]
    fields = ["image", "name", "description", ("price", "quantity"), "category"]
    list_filter = ["category"]
    search_fields = ["name"]


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ["product", "quantity", "created_time"]
    readonly_fields = ["created_time"]
    extra = 0


admin.site.register(ProductCategory)

from django.shortcuts import render

from products.models import Product, ProductCategory


def index(request):
    context = {"title": "Store"}
    return render(request, template_name="products/index.html", context=context)


def products(request):
    context = {
        "title": "Store - Каталог",
        "products": Product.objects.all(),
        "categories": ProductCategory.objects.all()
    }
    # добавити в контекс бд товарів, щоб добавити в шаблон
    return render(request, template_name="products/products.html", context=context)

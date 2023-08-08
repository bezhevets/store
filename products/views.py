from django.shortcuts import render, HttpResponseRedirect

from products.models import Product, ProductCategory, Basket


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


def basket_add(request, pk):
    product = Product.objects.get(id=pk)
    basket = Basket.objects.filter(user=request.user, product=product)

    if not basket.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = basket.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META["HTTP_REFERER"])


def basket_remove(request, pk):
    Basket.objects.get(id=pk).delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
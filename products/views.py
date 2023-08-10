from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from products.models import Product, ProductCategory, Basket

class IndexView(TemplateView):
    template_name = "products/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context["title"] = "Store"
        return context


def products(request, category_id=None, page_num=1):
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

    paginator = Paginator(products, per_page=3)
    products_paginator = paginator.page(page_num )

    context = {
        "title": "Store - Каталог",
        "products": products_paginator,
        "categories": ProductCategory.objects.all()
    }
    return render(request, template_name="products/products.html", context=context)


@login_required
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


@login_required
def basket_remove(request, pk):
    Basket.objects.get(id=pk).delete()
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
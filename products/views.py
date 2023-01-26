from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    Renders all poultry procucts
    """
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
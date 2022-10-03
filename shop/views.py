from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    product = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        product = product.filter(category=category)

    context = {
        'products': product,
        'category': category,
        'categories': categories,
    }
    return render(request, 'shop/product/list.html', context=context)

# Create your views here.


def product_detail(request, id, slug):
    product = get_object_or_404(Product, slug=slug, id=id, available=True)

    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
    }
    return render(request, 'shop/product/detail.html', context=context)

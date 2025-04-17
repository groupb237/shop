from django.shortcuts import render, redirect

import main.models as models


# Create your views here.

def home(request):
    return render(request, "index.html")


def category_list(request, category_id):
    products = models.Product.objects.filter(category_id=category_id)
    return render(request, "shop-categories.html", {"products": products})


def create_wishlist(request, product_id):
    user = request.user
    product = models.Product.objects.get(pk=product_id)
    models.Wishlist.objects.create(
        user=user,
        product=product
    )
    return redirect("/")


def list_wishlist(request):
    return render(request, template_name="wishlist.html")

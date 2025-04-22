from django.shortcuts import render, redirect, get_object_or_404

import main.models as models


# Create your views here.

def home(request):
    return render(request, "index.html")


def category_list(request, category_id):
    products = models.Product.objects.filter(category_id=category_id)
    return render(request, "shop-categories.html", {"products": products})


def create_wishlist(request, product_id):
    user = request.user
    if not models.Wishlist.objects.filter(product_id=product_id).exists():
        product = models.Product.objects.get(pk=product_id)
        models.Wishlist.objects.create(
            user=user,
            product=product
        )
        return redirect("/")
    else:
        return redirect("/")


def list_wishlist(request):
    return render(request, template_name="wishlist.html")


def delete_wishlist(request, pk):
    obj = get_object_or_404(models.Wishlist, pk=pk)
    if request.user.is_authenticated:
        obj.delete()
        return redirect("/wishlist/")


def product_detail(request, pk):
    obj = get_object_or_404(models.Product, pk=pk)
    if request.POST:
        if request.user.is_authenticated:
            name = request.user.username
            email = request.user.email
        else:
            name = request.POST.get("name")
            email = request.POST.get("email")
        rating = request.POST.get("rating")
        review = request.POST.get("review")
        models.Review.objects.create(
            product=obj,
            rating=rating,
            review=review,
            name=name,
            email=email
        )
    return render(request,
                  template_name="product-default.html",
                  context={"object": obj})

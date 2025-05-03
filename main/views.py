from idlelib.rpc import request_queue

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
    return redirect("/wishlist/")


def product_detail(request, pk):
    obj = get_object_or_404(models.Product, pk=pk)
    if request.user.is_authenticated:
        if not models.RecentView.objects.filter(user=request.user, product=obj).exists():
            models.RecentView.objects.create(
                user=request.user,
                product=obj
            )
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


def create_cart(request, product_id):
    product = get_object_or_404(models.Product, pk=product_id)
    if request.user.is_authenticated:
        user = request.user
        if models.Cart.objects.filter(user=user, is_active=True).exists():
            cart = models.Cart.objects.filter(user=user, is_active=True).last()
        else:
            cart = models.Cart.objects.create(
                user=user, total_sum=0
            )
        item = models.CartItem.objects.filter(cart=cart, product=product)
        if item.exists():
            item = item.first()
            item.quantity += 1
            item.save()
        else:
            models.CartItem.objects.create(
                cart=cart,
                product=product,
                quantity=1,
                price=product.price,
                sum=product.price
            )
        total_sum = 0
        for item in cart.items.all():
            total_sum += item.sum

        cart.total_sum = total_sum
        cart.save()

    return redirect("/")


def list_cart(request):
    if request.user.is_authenticated:
        cart = models.Cart.objects.filter(user=request.user, is_active=True).first()
        return render(request, "shopping-cart.html", context={"cart": cart})
    return redirect("/")


def delete_cart_item(request, item_id):
    item = get_object_or_404(models.CartItem, pk=item_id)
    if request.user.is_authenticated:
        item.delete()
    return redirect("/carts/list")


def delete_all_items(request):
    if request.user.is_authenticated:
        cart = models.Cart.objects.filter(user=request.user, is_active=True).first()
        cart.items.all().delete()
    return redirect("/carts/list")


def create_order(request):
    cart = models.Cart.objects.filter(user=request.user, is_active=True).first()
    if request.user.is_authenticated:
        if request.POST:
            f_name = request.POST.get("f_name")
            l_name = request.POST.get("l_name")
            m_name = request.POST.get("m_name")
            country = request.POST.get("country")
            street_address = request.POST.get("street_address")
            zip_code = request.POST.get("zip_code")
            city = request.POST.get("city")
            phone = request.POST.get("phone")
            email = request.POST.get("email")
            order_notes = request.POST.get("order_notes")
            payment = request.POST.get("payment")
            agree = request.POST.get("agree")
            if agree == "agree":
                agree = True
            else:
                agree = False

            models.Billing.objects.create(
                f_name=f_name, l_name=l_name, m_name=m_name,
                country=country, street_address=street_address, zip_code=zip_code,
                city=city, phone=phone, email=email, other_notes=order_notes, payment=payment, agree=agree
            )

            order = models.Order.objects.create(client=request.user, total_sum=0)

            total_sum = 0
            for item in cart.items.all():
                total_sum += item.sum
                models.OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.price,
                    sum=item.sum
                )
            order.total_sum = total_sum
            order.save()

            cart.is_active = False
            cart.save()

            return redirect("/")
    return render(request, template_name="checkout.html", context={"cart": cart})

from django.urls import path

import main.views as views

wishlist = [
    path("wishlist/", views.list_wishlist),
    path("wishlist/delete/<int:pk>", views.delete_wishlist),
    path("create/wishlist/<int:product_id>", views.create_wishlist)
]

product = [
    path("products/detail/<int:pk>", views.product_detail)
]

cart = [
    path("carts/list", views.list_cart),
    path("carts/items/delete", views.delete_all_items),
    path("carts/create/<int:product_id>", views.create_cart),
    path("carts/items/delete/<int:item_id>", views.delete_cart_item),
]

checkout = [
    path("checkout/list", views.create_order)
]

urlpatterns = [
    path("", views.home),
    path("category/<int:category_id>", views.category_list),
]

urlpatterns += wishlist + product + cart + checkout

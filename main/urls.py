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

urlpatterns = [
    path("", views.home),
    path("category/<int:category_id>", views.category_list),
]

urlpatterns += wishlist + product

from django.urls import path

import main.views as views

urlpatterns = [
    path("", views.home),
    path("wishlist/", views.list_wishlist),
    path("wishlist/delete/<int:pk>", views.delete_wishlist),
    path("category/<int:category_id>", views.category_list),
    path("create/wishlist/<int:product_id>", views.create_wishlist),
]

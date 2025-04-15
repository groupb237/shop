from django.urls import path

import main.views as views

urlpatterns = [
    path("", views.home),
    path("category/<int:category_id>", views.category_list),
    path("create/wishlist/<int:product_id>", views.create_wishlist),
]

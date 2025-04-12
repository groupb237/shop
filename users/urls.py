from django.urls import path

import users.views as views

urlpatterns = [
    path("register", views.register_user),
    path("login", views.login_user)
]

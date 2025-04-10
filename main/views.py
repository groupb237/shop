from django.shortcuts import render

import main.models as models
# Create your views here.

def home(request):
    return render(request, "index.html")

def category_list(request, category_id):
    products = models.Product.objects.filter(category_id=category_id)
    return render(request, "shop-categories.html", {"products": products})
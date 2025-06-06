import main.models as models


def variables(request):
    context = {
        "recent_views": models.RecentView.objects.all(),
        "banner": models.Banner.objects.all(),
        "products": models.Product.objects.all(),
        "category_list": models.Category.objects.filter(parent=None),
        "category_list_children": models.Category.objects.filter(parent__isnull=False)
    }
    return context

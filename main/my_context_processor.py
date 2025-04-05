import main.models as models


def variables(request):
    context = {
        "banner": models.Banner.objects.all(),
        "category_list": models.Category.objects.filter(parent=None),
        "category_list_children": models.Category.objects.filter(parent__isnull=False)
    }
    return context

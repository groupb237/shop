from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self",
                            on_delete=models.SET_NULL, null=True,
                            related_name="children")

    class MPTTMeta:
        order_insertion_by = ['name']

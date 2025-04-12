from django.db import models
from users.models import CustomUser


class Wishlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="wishlists")
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, related_name="wishlists")

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = "user_wishlists"
        ordering = ["user"]

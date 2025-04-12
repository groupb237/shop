from django.db import models

import users.models as users


class RecentView(models.Model):
    user = models.ForeignKey(users.CustomUser, on_delete=models.CASCADE, related_name="recent_views")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="recent_views")
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "recent_views"
        ordering = ["-added_at"]

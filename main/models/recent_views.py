from main.models.base import *
import users.models as users


class RecentView(BaseModel):
    user = models.ForeignKey(users.CustomUser, on_delete=models.CASCADE, related_name="recent_views")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="recent_views")

    def __str__(self):
        return f"{self.user}"

    class Meta:
        db_table = "recent_views"
        ordering = ["-added_at"]

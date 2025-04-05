from django.db import models


class Banner(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="banner/%Y-%m-%d")
    description = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "banners"
        ordering = ["-added_at"]

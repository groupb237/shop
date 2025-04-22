from main.models.base import *


class Banner(BaseModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="banner/%Y-%m-%d")
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "banners"
        ordering = ["-added_at"]

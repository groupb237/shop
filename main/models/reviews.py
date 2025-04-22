from main.models.base import *


class Review(BaseModel):
    product = models.ForeignKey("Product",
                                on_delete=models.CASCADE, related_name="reviews")
    rating = models.CharField(max_length=1)
    review = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-added_at",)

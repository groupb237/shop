from main.models.base import *
from mptt.models import TreeForeignKey


class Product(BaseModel):
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL,
        null=True, related_name="products")
    name = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to="products/%Y-%m-%d")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    amount = models.CharField(max_length=255)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
        ordering = ["-added_at"]


class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/images/%Y-%m-%d")

    def __str__(self):
        return self.product.name

    class Meta:
        db_table = "product_images"
        ordering = ["product"]

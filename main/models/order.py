import users.models as user
from main.models.base import *


class Order(BaseModel):
    client = models.ForeignKey(user.CustomUser, on_delete=models.SET_NULL, null=True, related_name="orders")
    total_sum = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return f"ordered to {self.client}"

    class Meta:
        db_table = "orders"
        ordering = ["-added_at"]


class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True, related_name="order_items")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=16, decimal_places=2)
    sum = models.DecimalField(max_digits=16, decimal_places=2)

    def __str__(self):
        return f"{self.order.id} item"

    class Meta:
        ordering = ["order"]

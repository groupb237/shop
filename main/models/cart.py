from main.models.base import *
import users.models as user_model


class Cart(BaseModel):
    user = models.ForeignKey(user_model.CustomUser,
                             on_delete=models.SET_NULL,
                             null=True, related_name="my_carts")
    is_active = models.BooleanField(default=True)
    total_sum = models.DecimalField(max_digits=16, decimal_places=2)


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=16, decimal_places=2)
    sum = models.DecimalField(max_digits=16, decimal_places=2)


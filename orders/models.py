from django.db import models
from shop.models import Item
from django.core.validators import MaxValueValidator, MinValueValidator


class Order(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    region = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zip_code = models.IntegerField(
        validators=[MaxValueValidator(98999), MinValueValidator(1)]
    )
    phone_number = models.CharField(max_length=20)
    comment = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        ordering = ("-created",)
        verbose_name_plural = "orders"


class OrderItem(models.Model):
    order_id = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE
    )
    item_id = models.ForeignKey(
        Item, related_name="order_items", on_delete=models.CASCADE
    )
    item_quantity = models.PositiveIntegerField(default=1)
    buy_price = models.DecimalField(max_digits=10, decimal_places=2)

    def get_cost(self):
        return self.buy_price * self.item_quantity

    class Meta:
        verbose_name_plural = "order items"
        ordering = ("order_id", "item_id")

from django.db import models
from shop.models import Item
from django.core.validators import (
    RegexValidator,
)


class Order(models.Model):
    phone_regex = RegexValidator(
        regex=r"^\+?3?8?\d{10}$",
        message="Має бути у форматі: '0501112233' з +38 за бажанням.",
    )
    zip_code_regex = RegexValidator(
        r"^\d{5}$", "Введіть 5 цифр вашого поштового індексу."
    )

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    region = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    zip_code = models.CharField(
        validators=[zip_code_regex],
        max_length=5,
    )
    phone_number = models.CharField(max_length=20, validators=[phone_regex])
    comment = models.TextField(blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    created = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True)

    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created",)
        verbose_name_plural = "orders"

    def __str__(self):
        return f"№{self.id} - {self.lastname} {self.firstname}"


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

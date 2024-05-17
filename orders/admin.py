from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "created",
        "firstname",
        "lastname",
        "email",
        "phone_number",
        "region",
        "address",
        "zip_code",
        "total_price",
        "is_processed",
    ]
    fields = [
        ("firstname", "lastname"),
        ("email", "phone_number"),
        ("region", "address", "zip_code"),
        "total_price",
        "comment",
        "is_processed",
        "updated",
    ]
    list_filter = ["created", "updated", "is_processed"]
    readonly_fields = ["total_price", "updated"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "item_id", "item_quantity", "buy_price"]
    fields = ["order_id", "item_id", "item_quantity", "buy_price"]
    readonly_fields = ["order_id", "item_id", "item_quantity", "buy_price"]

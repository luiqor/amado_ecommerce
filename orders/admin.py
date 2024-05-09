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
        "comment",
    ]
    fields = [
        ("firstname", "lastname"),
        ("email", "phone_number"),
        ("region", "address", "zip_code"),
        "total_price",
        "comment",
    ]
    list_filter = ["created"]
    readonly_fields = ["total_price"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["id", "order_id", "item_id", "item_quantity", "buy_price"]

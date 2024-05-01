from django.contrib import admin
from .models import Order, OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
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
        "created",
        ("firstname", "lastname"),
        ("email", "phone_number"),
        ("region", "address", "zip_code"),
        "total_price",
        "comment",
    ]
    list_filter = ["created"]


admin.site.register(OrderItem)

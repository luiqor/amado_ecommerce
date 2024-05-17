from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart
from shop.models import Item


def checkout(request):
    """
    Create an order and save it to the database. Update the item quantity
    for items in the database. If the quantity of the item is less than
    the order quantity, return an error message. Uses OrderCreateForm.
    Args:
        request: HttpRequest object
    Returns:
        HttpResponse object with rendered checkout.html template
        Context: form, total_price
    """
    cart = Cart(request)
    total_price = cart.get_total_price()
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = total_price
            order.save()
            for order_item in cart:
                item = Item.objects.get(id=order_item["item"].id)
                if order_item["qty"] > item.quantity:
                    form.add_error(
                        None,
                        "Вибачте, наразі на складі присутньо "
                        + str(item.quantity)
                        + " предмету "
                        + item.name,
                    )
                    return render(
                        request,
                        "checkout.html",
                        {
                            "form": form,
                            "total_price": total_price,
                        },
                    )
                OrderItem.objects.create(
                    order_id=order,
                    item_id=order_item["item"],
                    item_quantity=order_item["qty"],
                    buy_price=order_item["price"],
                )
                item.quantity -= order_item["qty"]
                if item.quantity == 0:
                    item.in_stock = False
                item.save()
            cart.clear()
            return redirect("order_success")
    else:
        form = OrderCreateForm()
    return render(
        request, "checkout.html", {"form": form, "total_price": total_price}
    )


def order_success(request):
    """Render the order_success.html template."""
    return render(request, "order_success.html")

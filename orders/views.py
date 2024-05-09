from django.shortcuts import render, redirect
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart


def checkout(request):
    cart = Cart(request)
    total_price = cart.get_total_price()
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.total_price = total_price
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order_id=order,
                    item_id=item["item"],
                    item_quantity=item["qty"],
                    buy_price=item["price"],
                )
            cart.clear()
            return redirect("order_success")
    else:
        form = OrderCreateForm()
    return render(
        request, "checkout.html", {"form": form, "total_price": total_price}
    )


def order_success(request):
    return render(request, "order_success.html")

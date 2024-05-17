from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .cart import Cart
from shop.models import Item


def cart_summary(request):
    """
    Renders the cart summary page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered cart summary page.
    """
    cart = Cart(request)
    cart.check_item_availability()
    return render(request, "cart/cart_summary.html", {"cart": cart})


def cart_add(request):
    """
    Adds an item to the cart.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the
        updated quantity in the cart.
    """
    cart = Cart(request)
    if request.method == "POST" and request.POST.get("action") == "post":
        item_id = int(request.POST.get("itemid"))

        item_qty = request.POST.get("itemqty")
        if item_qty is not None and item_qty != "":
            item_qty = int(item_qty)
        else:
            item_qty = 1

        item = get_object_or_404(Item, id=item_id)
        cart.add(item=item, qty=item_qty)

        cartqty = cart.__len__()
        response = JsonResponse({"qty": cartqty})
        return response


def cart_update(request):
    """
    Updates the quantity of an item in the cart.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the updated
        cart quantity and subtotal.
    """
    cart = Cart(request)
    if request.POST.get("action") == "post":
        item_id = int(request.POST.get("itemid"))
        item_qty = int(request.POST.get("itemqty"))
        cart.update(item=item_id, qty=item_qty)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({"qty": cartqty, "subtotal": carttotal})
        return response


def cart_delete(request):
    """
    Deletes an item from the cart.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: A JSON response containing the
        updated cart quantity and subtotal.
    """
    cart = Cart(request)
    if request.POST.get("action") == "post":
        item_id = int(request.POST.get("itemid"))
        cart.delete(item=item_id)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({"qty": cartqty, "subtotal": carttotal})
        return response

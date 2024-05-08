from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .cart import Cart
from shop.models import Item


def cart_summary(request):
    cart = Cart(request)
    return render(request, "cart/cart_summary.html", {'cart': cart})


def cart_add(request):
    cart = Cart(request)
    if request.method == 'POST' and request.POST.get('action') == 'post':
        item_id = int(request.POST.get('itemid'))
        print(item_id)
        item_qty = int(request.POST.get('itemqty'))
        item = get_object_or_404(Item, id=item_id)
        cart.add(item=item, qty=item_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
        return response

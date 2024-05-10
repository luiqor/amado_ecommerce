from decimal import Decimal

from shop.models import Item


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get("skey")
        if "skey" not in request.session:
            cart = self.session["skey"] = {}
        self.cart = cart

    def add(self, item, qty):
        item_id = str(item.id)
        if item_id in self.cart:
            self.cart[item_id]["qty"] += qty
        else:
            self.cart[item_id] = {"price": str(item.price), "qty": qty}

        self.save()

    def __iter__(self):
        item_ids = self.cart.keys()
        items = Item.objects.filter(id__in=item_ids)
        cart = self.cart.copy()

        for item in items:
            cart[str(item.id)]["item"] = item

        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["qty"]
            yield item

    def __len__(self):
        return sum(item["qty"] for item in self.cart.values())

    def get_total_price(self):
        return sum(
            Decimal(item["price"]) * item["qty"] for item in self.cart.values()
        )

    def update(self, item, qty):
        item_id = str(item)
        if item_id in self.cart:
            self.cart[item_id]["qty"] = qty
        self.save()

    def delete(self, item):
        item_id = str(item)

        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def clear(self):
        self.session["skey"] = {}

    def save(self):
        self.session.modified = True

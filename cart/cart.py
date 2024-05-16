from decimal import Decimal
from shop.models import Item


class Cart:
    def __init__(self, request):
        """
        Initializes the Cart object using the provided HTTP request.

        Args:
        request (HttpRequest): The HTTP request object containing
        client request data.
        """
        self.session = request.session
        cart = self.session.get("skey")
        if "skey" not in request.session:
            cart = self.session["skey"] = {}
        self.cart = cart

    def add(self, item, qty):
        """
        Adds an item to the cart or updates its quantity if
        it already exists.

        Args:
            item (Item): The item to be added to the cart.
            qty (int): The quantity of the item to be added
            to the cart.
        """
        item_id = str(item.id)
        if item_id in self.cart:
            self.cart[item_id]["qty"] += qty
        else:
            self.cart[item_id] = {"price": str(item.price), "qty": qty}

        self.save()

    def __iter__(self):
        """
        Iterates over the items in the cart.

        Yields:
            dict: A dictionary representing each item in the cart.
        """
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
        """
        Returns the total number of items in the cart.

        Returns:
            int: The total number of items in the cart.
        """
        return sum(item["qty"] for item in self.cart.values())

    def get_total_price(self):
        """
        Calculates and returns the total price of all items in the cart.

        Returns:
            Decimal: The total price of all items in the cart.
        """
        return sum(
            Decimal(item["price"]) * item["qty"] for item in self.cart.values()
        )

    def check_item_availability(self):
        """
        Checks the availability of items in the cart and updates
        their availability status.

        Returns:
            bool: True if the check is successful, False otherwise.
        """
        for item_id, item_data in self.cart.items():

            item = Item.objects.get(id=item_id)

            item_data["available"] = item.quantity

        return True

    def update(self, item, qty):
        """
        Updates the quantity of a specific item in the cart.

        Args:
            item (int): The ID of the item to be updated.
            qty (int): The new quantity of the item.
        """
        item_id = str(item)
        if item_id in self.cart:
            self.cart[item_id]["qty"] = qty
        self.save()

    def delete(self, item):
        """
        Deletes a specific item from the cart.

        Args:
            item (int): The ID of the item to be deleted.
        """
        item_id = str(item)

        if item_id in self.cart:
            del self.cart[item_id]
            self.save()

    def clear(self):
        """
        Clears all items from the cart.
        """
        self.session["skey"] = {}

    def save(self):
        """
        Saves the cart data to the session.
        """
        self.session.modified = True

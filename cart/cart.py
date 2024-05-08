from decimal import Decimal

from shop.models import Item


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}
        self.cart = cart
    
    
    def add(self, item, qty):
        """
        Adding and updating the users cart session data
        """
        item_id = str(item.id)

        if item_id in self.cart:
            self.cart[item_id]['qty'] = qty
        else:
            self.cart[item_id] = {'price': str(item.price), 'qty': qty}

        self.session.modified = True

    def __iter__(self):
        """
        Collect the item_id in the session data to query the database
        and return items
        """
        item_ids = self.cart.keys()
        items = item.items.filter(id__in=item_ids)
        cart = self.cart.copy()

        for item in items:
            cart[str(item.id)]['item'] = item

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        """
        Get the cart data and count the qty of items
        """
        return sum(item['qty'] for item in self.cart.values())
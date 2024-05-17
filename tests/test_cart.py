import pytest
from django.test import RequestFactory
from cart.views import cart_summary


@pytest.mark.django_db
def test_cart_summary_view_with_items(cart):
    """
    Checks that the cart page displays a list of all items
    added to the cart by the user.
    """
    request = RequestFactory().get('/cart/')
    request.session = cart.session

    response = cart_summary(request)
    assert response.status_code == 200

    assert b'Item1' in response.content
    assert b'Item2' in response.content


@pytest.mark.django_db
@pytest.mark.parametrize("item1_qty, item1_price, item2_qty, item2_price",
                         [(5, 10.00, 2, 20.00)])
def test_cart_summary_view_with_total_price(cart, item1_qty, item1_price,
                                            item2_qty, item2_price):
    """
    Checks that the cart page correctly calculates the total
    price of all items added to the cart by the user.
    """
    request = RequestFactory().get('/cart/')
    request.session = cart.session

    response = cart_summary(request)
    assert response.status_code == 200

    # Обчислення загальної вартості кошика
    total_price = (item1_qty * item1_price) + (item2_qty * item2_price)

    assert cart.get_total_price() == total_price

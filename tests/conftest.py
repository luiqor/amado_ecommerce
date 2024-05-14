import pytest
from shop.models import Category, Brand, Item
from cart.cart import Cart
from django.contrib.sessions.backends.base import SessionBase
from django.test import RequestFactory


@pytest.fixture
def categories(db):
    """Create categories for testing purposes."""
    category1 = Category.objects.create(name="Category1", slug="category1")
    category2 = Category.objects.create(name="Category2", slug="category2")
    category3 = Category.objects.create(name="Category3", slug="category3")
    return category1, category2, category3


@pytest.fixture
def brands(db):
    """Create brands for testing purposes."""
    brand1 = Brand.objects.create(name="Brand1", slug="brand1")
    brand2 = Brand.objects.create(name="Brand2", slug="brand2")
    return brand1, brand2


@pytest.fixture
def items_data(db, categories, brands):
    """Create items using categories and brands fixtures for
    testing purposes."""
    category1, category2, category3 = categories
    brand1, brand2 = brands

    item_image = "item_image.jpg"

    item1 = Item.objects.create(
        name="Item1",
        slug="item1",
        price=10.00,
        photo=item_image,
        quantity=10,
        in_stock=True,
        stars=4,
        category=category1,
        brand=brand1,
    )
    item2 = Item.objects.create(
        name="Item2",
        slug="item2",
        price=20.00,
        photo=item_image,
        quantity=5,
        in_stock=True,
        stars=3,
        category=category1,
        brand=brand2,
    )
    item3 = Item.objects.create(
        name="Item3",
        slug="item3",
        price=15.00,
        photo=item_image,
        quantity=2,
        in_stock=True,
        stars=5,
        category=category2,
        brand=brand1,
    )
    item4 = Item.objects.create(
        name="Item4",
        slug="item4",
        price=25.00,
        photo=item_image,
        quantity=7,
        in_stock=True,
        stars=2,
        category=category2,
        brand=brand2,
    )
    item5 = Item.objects.create(
        name="Item5",
        slug="item5",
        price=30.00,
        photo=item_image,
        quantity=4,
        in_stock=True,
        stars=1,
        category=category3,
        brand=brand2,
    )
    item6 = Item.objects.create(
        name="Item6",
        slug="item6",
        price=35.00,
        photo=item_image,
        quantity=3,
        in_stock=True,
        stars=3,
        category=category2,
        brand=brand1,
    )
    return [item1, item2, item3, item4, item5, item6]


@pytest.fixture
def cart(items_data):
    """Fixture for creating a Cart instance with specific items."""
    session = SessionBase()
    session['_auth_user_id'] = 1  # You may need to set this depending on your session data

    item1, item2, *_ = items_data

    session['skey'] = {
        str(item1.id): {'qty': 5},
        str(item2.id): {'qty': 2},
    }

    request = RequestFactory().post('/dummy-url')  # You can use any dummy URL here
    request.session = session

    return Cart(request)

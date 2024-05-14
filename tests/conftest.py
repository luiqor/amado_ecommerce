import pytest
from shop.models import Category, Brand, Item
from orders.models import Order, OrderItem


@pytest.fixture(autouse=True)
def category(db):
    return Category.objects.create(name="Test Category", slug="test-category")


@pytest.fixture(autouse=True)
def brand(db):
    return Brand.objects.create(name="Test Brand", slug="test-brand")


@pytest.fixture(autouse=True)
def item(db, category, brand):
    return Item.objects.create(
        name="Test Item",
        slug="test-item",
        price=1300.99,
        photo="path/to/photo.jpg",
        description="Test Description",
        quantity=5,
        in_stock=True,
        stars=4,
        category=category,
        brand=brand,
    )


@pytest.fixture(autouse=True)
def order(db):
    return Order.objects.create(
        firstname="John",
        lastname="Doe",
        email="testuser@example.com",
        region="kyiv",
        address="123 Test St",
        zip_code="12345",
        phone_number="0501112233",
        comment="Test Comment",
        total_price=2500.55,
        is_processed=False,
    )


@pytest.fixture(autouse=True)
def order_item(db, order, item):
    return OrderItem.objects.create(
        order_id=order, item_id=item, item_quantity=2, buy_price=2500.55
    )

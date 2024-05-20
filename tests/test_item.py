import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_item_view(items_data, categories, brands):
    """Test the item view."""
    client = Client()
    item = items_data[0]
    url = reverse("item", kwargs={"slug": item.slug, "item_id": item.id})

    response = client.get(url)
    assert response.status_code == 200
    assert "item" in response.context

    item = response.context["item"]
    assert item.name == "Item1"
    assert item.photo == "test_image.jpg"
    assert item.slug == "item1"
    assert item.price == 10.00
    assert item.quantity == 10
    assert item.in_stock
    assert item.stars == 4
    assert item.category.slug == categories[0].slug
    assert item.brand.slug == brands[0].slug


@pytest.mark.django_db
@pytest.mark.parametrize(
    "in_stock, expected_message",
    [(True, "В наявності"), (False, "Немає в наявності")],
)
def test_item_availability(items_data, in_stock, expected_message):
    """Test if the correct availability message is displayed
    on the item page."""
    client = Client()
    item = items_data[0]
    url = reverse("item", kwargs={"slug": item.slug, "item_id": item.id})

    response = client.get(url)
    assert response.status_code == 200

    if item.in_stock == in_stock:
        assert expected_message.encode("utf-8") in response.content


@pytest.mark.django_db
def test_add_to_cart_button_visibility(items_data):
    """Test if the 'Add to Cart' button is visible on the item page."""
    # Create a client
    client = Client()
    item = items_data[0]

    url = reverse("item", kwargs={"slug": item.slug, "item_id": item.id})
    response = client.get(url)

    assert response.status_code == 200

    if item.in_stock:
        assert "Додати у кошик".encode("utf-8") in response.content
    else:
        assert "Додати у кошик".encode("utf-8") not in response.content


@pytest.mark.django_db
def test_add_to_cart(cart, items_data):
    """Test if item is added to the cart."""
    item = items_data[0]
    cart.add(item, 1)

    assert str(item.id) in cart.cart
    assert cart.cart[str(item.id)]["qty"] == 6


@pytest.mark.django_db
def test_item_quantity_display_in_cart_template(cart, items_data):
    """Test if the quantity of items is correctly
    displayed in the cart template."""
    client = Client()
    item = items_data[0]
    url = reverse("item", kwargs={"slug": item.slug, "item_id": item.id})

    response = client.get(url)
    assert response.status_code == 200

    expected_quantity_display = cart.cart[str(item.id)]["qty"]
    assert expected_quantity_display == 5

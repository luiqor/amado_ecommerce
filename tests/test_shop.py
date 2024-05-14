import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_shop_view_status_code(client):
    response = client.get(reverse("shop"))
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.parametrize(
    "category, expected_count, items_per_page",
    [
        ("category1", 2, 2),
        ("category3", 1, 5),
        ("category2", 2, 2),
        ("category2", 3, 5),
    ],
)
def test_shop_view_filter_by_category(
    client, items_data, category, expected_count, items_per_page
):
    """Test that the shop view has only items in specified category.
    Items per page defines maximum number of items recieved."""
    response = client.get(
        reverse("shop"),
        {"category": category, "items_per_page": items_per_page},
    )
    assert response.status_code == 200
    assert len(response.context["items"]) == expected_count


@pytest.mark.django_db
def test_shop_view_sort_by_price(client, items_data):
    """Ensure items are sorted by price.
    Items with lower price should come first."""
    response = client.get(reverse("shop"), {"sort_by": "price"})
    assert response.status_code == 200
    items = list(response.context["items"])
    for i in range(len(items) - 1):
        assert items[i].price <= items[i + 1].price


@pytest.mark.django_db
def test_shop_view_sort_by_newest(client, items_data):
    """Ensure items are sorted by newest.
    The item created last should come first."""
    response = client.get(reverse("shop"), {"sort_by": "newest"})
    assert response.status_code == 200
    items = list(response.context["items"])
    for i in range(len(items) - 1):
        assert items[i].created >= items[i + 1].created


@pytest.mark.django_db
def test_shop_view_sort_by_popular(client, items_data):
    """Ensure items are sorted by popular.
    The item with more stars should come first."""
    response = client.get(reverse("shop"), {"sort_by": "popular"})
    assert response.status_code == 200
    items = list(response.context["items"])
    for i in range(len(items) - 1):
        assert items[i].stars >= items[i + 1].stars


@pytest.mark.parametrize(
    "items_per_page, page", [(2, 1), (2, 2), (5, 1), (5, 5)]
)
def test_shop_view_pagination(client, items_data, items_per_page, page):
    """Ensure the shop view contains specified number of items on each page
    or less if there are not enough items in db."""
    response = client.get(
        reverse("shop"), {"items_per_page": items_per_page, "page": page}
    )
    assert response.status_code == 200
    assert len(response.context["items"]) <= items_per_page

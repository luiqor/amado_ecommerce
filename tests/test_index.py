import pytest
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_home_view(items_data):
    """Test home view."""
    client = Client()
    response = client.get('/')

    assert response.status_code == 200
    assert 'items' in response.context

    top_rated_items = response.context['items']

    assert len(top_rated_items) == 6

    assert top_rated_items[0].name == "Item3"
    assert top_rated_items[1].name == "Item1"
    assert top_rated_items[2].name == "Item2" or "Item6"
    assert top_rated_items[3].name == "Item2" or "Item6"
    assert top_rated_items[4].name == "Item4"
    assert top_rated_items[5].name == "Item5"

    assert top_rated_items[0].stars == 5
    assert top_rated_items[1].stars == 4
    assert top_rated_items[2].stars == 3
    assert top_rated_items[3].stars == 3
    assert top_rated_items[4].stars == 2
    assert top_rated_items[5].stars == 1


def test_item_page_navigation(items_data):
    """Test if clicking on each item in the template
    navigates to the correct page."""
    client = Client()

    for item in items_data:
        url = reverse('item', kwargs={'slug': item.slug, 'item_id': item.id})
        response = client.get(url)

        assert response.status_code == 200

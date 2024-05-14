import pytest
from shop.forms import FilterForm


@pytest.mark.django_db
def test_form_initialization(categories, brands):
    """Ensures that the category and brands fields have the correct choices"""
    form = FilterForm()

    assert form.fields["category"].choices == [
        (category.slug, category.name) for category in categories
    ]
    assert form.fields["brands"].choices == [
        (brand.slug, brand.name) for brand in brands
    ]

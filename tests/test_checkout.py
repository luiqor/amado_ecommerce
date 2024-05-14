import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_checkout_view_status_code(client):
    response = client.get(reverse("checkout"))
    assert response.status_code


@pytest.mark.django_db
@pytest.mark.parametrize(
    "firstname, lastname, email, region, address, "
    "zip_code, phone_number, comment",
    [
        (
            "John",
            "Doe",
            "john@example.com",
            "Some Region",
            "123 Some St",
            "12345",
            "0501234567",
            "Please deliver between 9 AM and 5 PM.",
        ),
        (
            "Jane",
            "Doe",
            "jane@example.com",
            "Another Region",
            "456 Another St",
            "67890",
            "+380507654321",
            "",
        ),
    ],
)
def test_checkout_view_success(
    client,
    items_data,
    firstname,
    lastname,
    email,
    region,
    address,
    zip_code,
    phone_number,
    comment,
):
    """Test successful checkout with valid form data."""
    response = client.post(
        reverse("checkout"),
        data={
            "firstname": firstname,
            "lastname": lastname,
            "email": email,
            "region": region,
            "address": address,
            "zip_code": zip_code,
            "phone_number": phone_number,
            "comment": comment,
        },
    )

    assert response.status_code == 302


@pytest.mark.django_db
def test_checkout_view_invalid_form(client, items_data):
    response = client.post(
        reverse("checkout"),
        data={
            "firstname": "",
            "lastname": "",
            "email": "invalid-email",
            "region": "",
            "address": "",
            "zip_code": "123",
            "phone_number": "invalid-phone",
        },
    )

    assert response.status_code == 200  # OK response with invalid form data
    assert "form" in response.context
    form = response.context["form"]
    assert not form.is_valid()
    assert "firstname" in form.errors
    assert "lastname" in form.errors
    assert "email" in form.errors
    assert "region" in form.errors
    assert "address" in form.errors
    assert "zip_code" in form.errors
    assert "phone_number" in form.errors

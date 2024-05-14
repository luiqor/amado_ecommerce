from django import forms
from .models import Category, Brand


class FilterForm(forms.Form):
    """Form for filtering items by category, brand, and price."""

    category = forms.ChoiceField(
        choices=[],
        required=False,
        widget=forms.RadioSelect(
            attrs={"class": "form-check-input display-none"}
        ),
    )
    brands = forms.MultipleChoiceField(
        choices=[],
        required=False,
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input"}
        ),
    )
    min_price = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(
            attrs={"class": "min-price-input", "id": "min_price"}
        ),
    )
    max_price = forms.IntegerField(
        required=False,
        widget=forms.HiddenInput(
            attrs={"class": "max-price-input", "id": "max_price"}
        ),
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with choices for categories and brands.
        Choices are dynamically generated from the database.
        """
        super().__init__(*args, **kwargs)

        self.fields["category"].choices = [
            (category.slug, category.name)
            for category in Category.objects.all()
        ]
        self.fields["brands"].choices = [
            (brand.slug, brand.name) for brand in Brand.objects.all()
        ]


class TopBarForm(forms.Form):
    """Form for sorting items by price, newest, and popular."""

    sort_by = forms.ChoiceField(
        choices=[
            ("price", "Price"),
            ("newest", "Newest"),
            ("popular", "Popular"),
        ],
        widget=forms.Select(attrs={"onchange": "submit(this.form)"}),
    )
    items_per_page = forms.ChoiceField(
        choices=[
            (2, "2"),
            (5, "5"),
            (12, "12"),
            (24, "24"),
            (48, "48"),
            (96, "96"),
        ],
        widget=forms.Select(attrs={"onchange": "submit(this.form)"}),
    )

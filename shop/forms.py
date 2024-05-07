from django import forms
from .models import Item, Brand, Category


class ItemFilterForm(forms.Form):
    min_price = forms.FloatField(required=False)
    max_price = forms.FloatField(required=False)
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        required=False,
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
    )

    def filter_items(self):
        items = Item.objects.all()
        if self.cleaned_data.get("min_price"):
            items = items.filter(price__gte=self.cleaned_data["min_price"])
        if self.cleaned_data.get("max_price"):
            items = items.filter(price__lte=self.cleaned_data["max_price"])
        if self.cleaned_data.get("brand"):
            items = items.filter(brand=self.cleaned_data["brand"])
        if self.cleaned_data.get("category"):
            items = items.filter(category=self.cleaned_data["category"])
        return items

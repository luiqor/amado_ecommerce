from django import forms


class TopBarForm(forms.Form):
    select = forms.ChoiceField(
        choices=[
            ("price", "Price"),
            ("newest", "Newest"),
            ("popular", "Popular"),
        ],
        widget=forms.Select(
            attrs={"onchange": "submitFormWithFilterParams(this.form)"}
        ),
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
        widget=forms.Select(
            attrs={"onchange": "submitFormWithFilterParams(this.form)"}
        ),
    )

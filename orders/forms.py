from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "firstname",
            "lastname",
            "email",
            "region",
            "address",
            "zip_code",
            "phone_number",
            "comment",
        ]
        widgets = {
            "firstname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "first_name",
                    "placeholder": "First Name",
                    "required": True,
                }
            ),
            "lastname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "last_name",
                    "placeholder": "Last Name",
                    "required": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "Email",
                }
            ),
            "region": forms.Select(
                attrs={"class": "form-control w-100", "id": "region"},
                choices=[
                    ("vinnytsia", "Vinnytsia Region"),
                    ("zhytomyr", "Zhytomyr Region"),
                    ("ivanofrankivsk", "Ivano-Frankivsk Region"),
                    ("kyivregion", "Kyiv Region"),
                    ("lviv", "Lviv Region"),
                    ("poltava", "Poltava Region"),
                    ("ternopil", "Ternopil Region"),
                    ("khmelnytskyi", "Khmelnytskyi Region"),
                    ("cherkasy", "Cherkasy Region"),
                    ("chernivtsi", "Chernivtsi Region"),
                    ("chernihiv", "Chernihiv Region"),
                ],
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "id": "street_address",
                    "placeholder": "Address",
                    "required": True,
                }
            ),
            "zip_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "zipCode",
                    "placeholder": "Zip Code",
                }
            ),
            "phone_number": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "id": "phone_number",
                    "placeholder": "Phone No",
                    "min": 0,
                }
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control w-100 h-50",
                    "id": "comment",
                    "cols": 30,
                    "rows": 10,
                    "placeholder": "Leave a comment about your order",
                }
            ),
        }

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
                    "placeholder": "Ім'я",
                    "required": True,
                }
            ),
            "lastname": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "last_name",
                    "placeholder": "Прізвище",
                    "required": True,
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "id": "email",
                    "placeholder": "Скринька",
                }
            ),
            "region": forms.Select(
                attrs={"class": "form-control w-100", "id": "region"},
                choices=[
                    ("vinnytsia", "Вінницька область"),
                    ("zhytomyr", "Житомирська область"),
                    ("ivanofrankivsk", "Івано-Франківська область"),
                    ("kyiv", "Київська область та місто"),
                    ("lviv", "Львівська область"),
                    ("poltava", "Полтавська область"),
                    ("ternopil", "Тернопільська область"),
                    ("khmelnytskyi", "Хмельницька область"),
                    ("cherkasy", "Черкаська область"),
                    ("chernivtsi", "Чернівецька область"),
                    ("chernihiv", "Чернігівська область"),
                ],
            ),
            "address": forms.TextInput(
                attrs={
                    "class": "form-control mb-3",
                    "id": "street_address",
                    "placeholder": "Адреса",
                    "required": True,
                }
            ),
            "zip_code": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "zipCode",
                    "placeholder": "Поштовий індекс",
                }
            ),
            "phone_number": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "phone_number",
                    "placeholder": "Номер телефону",
                }
            ),
            "comment": forms.Textarea(
                attrs={
                    "class": "form-control w-100 h-50",
                    "id": "comment",
                    "cols": 30,
                    "rows": 10,
                    "placeholder": "Залиште коментар до замовлення",
                }
            ),
        }

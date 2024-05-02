from django.shortcuts import render
from .models import Category, Brand, Item


def home(request):
    return render(request, "index.html")


def shop(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    for item in items:
        item.stars_range = range(item.stars)
        item.empty_stars_range = range(5 - item.stars)

    return render(
        request,
        "shop.html",
        context={"categories": categories, "brands": brands, "items": items},
    )

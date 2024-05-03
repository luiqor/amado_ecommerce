from django.shortcuts import render
from django.db.models import Min, Max
from .models import Category, Brand, Item


def home(request):
    top_rated_items = Item.objects.order_by("-stars")[:9]

    return render(request, "index.html", context={"items": top_rated_items})


def shop(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    brands = Brand.objects.all()

    min_price = None
    max_price = None
    smallest_price = items.aggregate(Min("price"))["price__min"]
    biggest_price = items.aggregate(Max("price"))["price__max"]

    if request.method == "POST":
        items, min_price, max_price = filter_items(request, items)

    return render(
        request,
        "shop.html",
        context={
            "categories": categories,
            "brands": brands,
            "items": items,
            "smallest_price": smallest_price,
            "biggest_price": biggest_price,
            "min_price": round(min_price) if min_price else smallest_price,
            "max_price": round(max_price) if max_price else biggest_price,
        },
    )


def filter_items(request, items):
    category = request.POST.get("category")
    brand = request.POST.get("brand")
    min_price = request.POST.get("min_price")
    max_price = request.POST.get("max_price")

    if min_price and max_price:
        min_price = float(min_price)
        max_price = float(max_price)

    if category:
        items = items.filter(category__name=category)
    if brand:
        items = items.filter(brand__name=brand)
    if min_price and max_price:
        items = items.filter(price__range=(min_price, max_price))

    return items, min_price, max_price


def item(request, slug, item_id):
    item = Item.objects.get(id=item_id)

    item.stars_range = range(item.stars)
    item.empty_stars_range = range(5 - item.stars)
    return render(request, "item.html", context={"item": item})

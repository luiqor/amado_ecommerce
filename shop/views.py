from django.shortcuts import render
from django.db.models import Min, Max
from .models import Category, Brand, Item
from django.core.paginator import Paginator
from .forms import TopBarForm, FilterForm


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

    filter_form = FilterForm(request.GET)
    if filter_form.is_valid():
        print(filter_form.cleaned_data)
        if filter_form.cleaned_data["category"]:
            items = items.filter(
                category__slug=filter_form.cleaned_data["category"]
            )

        if filter_form.cleaned_data["brands"]:
            items = items.filter(
                brand__slug__in=filter_form.cleaned_data["brands"]
            )

        if filter_form.cleaned_data["min_price"]:
            items = items.filter(
                price__gte=filter_form.cleaned_data["min_price"]
            )

        if filter_form.cleaned_data["max_price"]:
            items = items.filter(
                price__lte=filter_form.cleaned_data["max_price"]
            )

    if request.method == "GET":
        sort_by = request.GET.get("select", "newest").strip()
        if sort_by == "price":
            items = items.order_by("price")
        elif sort_by == "newest":
            items = items.order_by("-created")
        elif sort_by == "popular":
            items = items.order_by("-stars")

    items_per_page = request.GET.get("items_per_page", 2)
    paginator = Paginator(items, items_per_page)
    page_number = request.GET.get("page")
    paginated_items = paginator.get_page(page_number)
    topbar_form = TopBarForm(request.GET)
    return render(
        request,
        "shop.html",
        context={
            "categories": categories,
            "brands": brands,
            "items": paginated_items,
            "smallest_price": smallest_price,
            "biggest_price": biggest_price,
            "min_price": round(min_price) if min_price else smallest_price,
            "max_price": round(max_price) if max_price else biggest_price,
            "items_per_page": items_per_page,
            "total_items": paginator.count,
            "sort_by": sort_by,
            "filter_form": filter_form,
            "topbar_form": topbar_form,
        },
    )


def item(request, slug, item_id):
    item = Item.objects.get(id=item_id)

    item.stars_range = range(item.stars)
    item.empty_stars_range = range(5 - item.stars)
    return render(request, "item.html", context={"item": item})

from django.shortcuts import render
from django.db.models import Min, Max
from .models import Item
from django.core.paginator import Paginator
from .forms import TopBarForm, FilterForm


def home(request):
    top_rated_items = Item.objects.order_by("-stars")[:9]

    return render(request, "index.html", context={"items": top_rated_items})


def shop(request):
    """
    Display all items with filtering, sorting options and pagination.
    Use FilterForm to filter items by category, brand, and price.
    Use TopBarForm to sort items and set items per page. Sets min_price
    and max_price for price range slider based on the user's selection.
    If the user doesn't select any price range, the default values are
    the smallest and biggest prices of the items from db.
    Args:
        request: HttpRequest object
    Returns:
        HttpResponse object with rendered shop.html template
        Context: items, smallest_price, biggest_price, min_price, max_price,
        items_per_page, total_items, sort_by, filter_form, topbar_form,
        last_selected_category, last_selected_brands
    """
    items = Item.objects.all()
    last_selected_category = None
    last_selected_brands = []
    min_price = None
    max_price = None
    smallest_price = items.aggregate(Min("price"))["price__min"]
    biggest_price = items.aggregate(Max("price"))["price__max"]

    filter_form = FilterForm(request.GET)
    topbar_form = TopBarForm(request.GET)
    if request.method == "GET":
        if filter_form.is_valid():
            filters = {
                "category": "category__slug",
                "brands": "brand__slug__in",
                "min_price": "price__gte",
                "max_price": "price__lte",
            }
            for key, value in filters.items():
                if filter_form.cleaned_data[key]:
                    items = items.filter(
                        **{value: filter_form.cleaned_data[key]}
                    )  # {category__slug="beds",..}
            last_selected_category = filter_form.cleaned_data["category"]
            last_selected_brands = filter_form.cleaned_data["brands"]

        sort_by = request.GET.get("sort_by", "price").strip()
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

    return render(
        request,
        "shop.html",
        context={
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
            "last_selected_category": last_selected_category,
            "last_selected_brands": last_selected_brands,
        },
    )


def item(request, slug, item_id):
    item = Item.objects.get(id=item_id)

    item.stars_range = range(item.stars)
    item.empty_stars_range = range(5 - item.stars)
    return render(request, "item.html", context={"item": item})

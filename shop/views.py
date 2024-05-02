from django.shortcuts import render
from .models import Category, Brand


def home(request):
    return render(request, "index.html")


def shop(request):
    categories = Category.objects.all()
    brands = Brand.objects.all()
    return render(
        request,
        "shop.html",
        context={"categories": categories, "brands": brands},
    )

"""
URL configuration for amado_ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from shop.views import home, shop, item
from orders.views import checkout, order_success


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("shop/", shop, name="shop"),
    path("<slug:slug>/<int:item_id>", item, name="item"),
    path("cart/", include("cart.urls", namespace="cart")),
    path("checkout/", checkout, name="checkout"),
    path("order_success/", order_success, name="order_success"),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

from django.contrib import admin
from .models import Category, Brand, Item


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_field = {'slug':('name',)}


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'photo', 'description', 
                    'quantity', 'in_stock', 'stars', 'category', 'brand']
    list_filter = ['category', 'brand', 'in_stock',]
    list_editable = ['price', 'in_stock', 'photo', 'description', 
                     'quantity', 'stars']
    prepopulated_fields = {'slug': ('name',)}

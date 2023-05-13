from django.contrib import admin
from .models import Category, Product, Image


class InlineImage(admin.TabularInline):
    model = Image
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = [
        'id',
        'name',
        'slug',
    ]
    list_display_links = [
        'id',
        'name',
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',),
    }
    list_display = [
        'id',
        'name',
        'category',
        'available',
    ]
    list_display_links = [
        'id',
        'name',
    ]
    list_editable = [
        'available',
    ]
    inlines = [
        InlineImage,
    ]

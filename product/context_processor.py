from .models import Category
from django.http import HttpRequest


def categories(request: HttpRequest) -> dict:
    category = Category.objects.all()
    return {
        'categories': category
    }

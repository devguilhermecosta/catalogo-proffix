from .models import Information
from django.http import HttpRequest


def information(request: HttpRequest) -> dict:
    informs = Information.objects.first()
    return {
        'information': informs
    }

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Information, Docs


def contact(request: HttpRequest) -> HttpResponse:
    information = Information.objects.first()

    docs = None

    if information:
        docs = Docs.objects.filter(
            company__id=information.id
        ).first()

    return render(
        request,
        'information/pages/contact.html',
        context={
            'information': information,
            'docs': docs
        }
    )

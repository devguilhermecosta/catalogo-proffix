from django.urls import path
from . import views


app_name: str = 'information'

urlpatterns: list = [
    path('', views.contact, name="contact"),
]

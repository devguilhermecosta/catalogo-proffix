from django.urls import path
from . import views


app_name: str = 'product'

urlpatterns: list = [
    path('', views.ProductList.as_view(), name='products'),
]

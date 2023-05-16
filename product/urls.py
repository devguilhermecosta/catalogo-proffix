from django.urls import path
from . import views


app_name: str = 'product'

urlpatterns: list = [
    path('', views.product_list, name='products'),
    path('<str:slug>/', views.product_detail, name='detail'),
    path('produtos/<str:slug>/', views.product_category, name='category'),
]

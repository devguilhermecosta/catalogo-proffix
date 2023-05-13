from django.views.generic import ListView
from product.models import Product


class ProductList(ListView):
    template_name = 'product/pages/products.html'
    queryset = Product.objects.filter(available=True)
    context_object_name = 'products'

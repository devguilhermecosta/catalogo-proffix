from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest
from product.models import Product, Image


class ProductList(ListView):
    template_name = 'product/pages/products.html'
    queryset = Product.objects.filter(available=True)
    context_object_name = 'products'


def product_detail(request: HttpRequest, slug: str):
    product: Product = get_object_or_404(Product,
                                         available=True,
                                         slug=slug)
    images: Image = Image.objects.filter(
        product=product,
    )

    return render(
        request,
        'product/pages/product_detail.html',
        context={
            'product': product,
            'images': images,
        }
    )

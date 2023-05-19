from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpRequest, HttpResponse
from product.models import Product, Image
from utils.pagination.pagination import make_pagination
import os


PER_PAGE = int(os.environ.get('PER_PAGE', 8))


def product_list(request: HttpRequest) -> HttpResponse:
    products = Product.objects.filter(available=True).order_by('-id')

    page_obj, pagination_range = make_pagination(request,
                                                 products,
                                                 PER_PAGE,
                                                 )

    return render(
        request,
        'product/pages/products.html',
        context={
            'products': page_obj,
            'pagination_range': pagination_range,
            }
    )


def product_detail(request: HttpRequest, slug: str):
    product: Product = get_object_or_404(Product,
                                         available=True,
                                         slug=slug)
    images: Image = Image.objects.filter(
        product=product,
    )
    link = 'https://catalogo.proffixortopedia.com' + reverse(
        'product:detail', args=(product.slug,)
        )

    return render(
        request,
        'product/pages/product_detail.html',
        context={
            'product': product,
            'images': images,
            'link': link,
        }
    )


def product_category(request, slug) -> HttpResponse:
    products = Product.objects.filter(category__slug=slug).order_by('-id')

    page_object, pagination_range = make_pagination(request,
                                                    products,
                                                    PER_PAGE)

    return render(
        request,
        'product/pages/products.html',
        context={
            'products': page_object,
            'pagination_range': pagination_range,
        }
    )

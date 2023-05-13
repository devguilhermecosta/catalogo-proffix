from django.test import TestCase
from django.urls import reverse, resolve, ResolverMatch
from django.http import HttpResponse
from product.views import ProductList


class ProductTests(TestCase):
    def test_products_url_is_correct(self) -> None:
        url: str = '/'

        self.assertEqual(url, reverse('product:products'))

    def test_products_load_correct_view(self) -> None:
        url: str = reverse('product:products')
        response: ResolverMatch = resolve(url)

        self.assertEqual(ProductList, response.func.view_class)

    def test_products_load_correct_template(self) -> None:
        url: str = reverse('product:products')
        response: HttpResponse = self.client.get(url)

        self.assertTemplateUsed(response, 'product/pages/products.html')

    def test_products_load_correct_context_data(self) -> None:
        pass

from django.test import TestCase
from django.test import override_settings
from django.urls import reverse, resolve, ResolverMatch
from django.http import HttpResponse
from product import views
from .product_test_base import make_product_range
import shutil
import contextlib


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
class ProductTests(TestCase):
    def setUp(self):
        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)
        return super().setUp()

    def test_products_url_is_correct(self) -> None:
        url: str = '/'

        self.assertEqual(url, reverse('product:products'))

    def test_product_url_status_code_200(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:products')
        )

        self.assertEqual(response.status_code, 200)

    def test_products_load_correct_view(self) -> None:
        url: str = reverse('product:products')
        response: ResolverMatch = resolve(url)

        self.assertEqual(views.product_list, response.func)

    def test_products_load_correct_template(self) -> None:
        url: str = reverse('product:products')
        response: HttpResponse = self.client.get(url)

        self.assertTemplateUsed(response, 'product/pages/products.html')

    def test_products_load_correct_context_data(self) -> None:
        make_product_range(3)

        response: HttpResponse = self.client.get(
            reverse('product:products')
        )

        content: str = response.content.decode('utf-8')

        self.assertIn('name of product 0', content)
        self.assertIn('name of product 1', content)
        self.assertIn('name of product 2', content)

    def test_products_load_no_registred_product_if_no_prodducts(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:products')
        )
        content: str = response.content.decode('utf-8')

        self.assertIn(
            'No momento estamos sem produtos disponíveis nesta categoria',
            content,
            )

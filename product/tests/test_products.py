from django.test import TestCase
from django.test import override_settings
from django.urls import reverse, resolve, ResolverMatch
from django.http import HttpResponse
from product import views
from information.tests.base_information import make_information
from .product_test_base import make_product_range
from unittest.mock import patch
import shutil
import contextlib


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
class ProductTests(TestCase):
    def setUp(self):
        self.path = 'product:products'
        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)
        return super().setUp()

    def test_products_url_is_correct(self) -> None:
        url: str = '/'

        self.assertEqual(url, reverse(self.path))

    def test_product_url_status_code_200(self) -> None:
        response: HttpResponse = self.client.get(
            reverse(self.path)
        )

        self.assertEqual(response.status_code, 200)

    def test_products_load_correct_view(self) -> None:
        url: str = reverse(self.path)
        response: ResolverMatch = resolve(url)

        self.assertEqual(views.product_list, response.func)

    def test_products_load_correct_template(self) -> None:
        url: str = reverse(self.path)
        response: HttpResponse = self.client.get(url)

        self.assertTemplateUsed(response, 'product/pages/products.html')

    def test_products_load_correct_context_data(self) -> None:
        make_product_range(3)

        response: HttpResponse = self.client.get(
            reverse(self.path)
        )

        content: str = response.content.decode('utf-8')

        self.assertIn('name of product 0', content)
        self.assertIn('name of product 1', content)
        self.assertIn('name of product 2', content)

    def test_products_load_no_registred_product_if_no_prodducts(self) -> None:
        response: HttpResponse = self.client.get(
            reverse(self.path)
        )
        content: str = response.content.decode('utf-8')

        self.assertIn(
            'No momento estamos sem produtos disponíveis nesta categoria',
            content,
            )

    def test_products_page_is_paginated(self) -> None:
        ''' created 16 product objects '''
        make_product_range(16)

        path = 'product.views.PER_PAGE'

        ''' test with 4 products per page '''
        with patch(path, new=4):
            response_1: HttpResponse = self.client.get(
                    reverse(self.path)
                )
            products_length_1 = len(response_1.context['products'])
            total_pages_1 = (
                response_1.context['pagination_range'].get('total_pages')
            )
            self.assertEqual(products_length_1, 4)
            self.assertEqual(total_pages_1, 4)

        with patch(path, new=10):
            response_2: HttpResponse = self.client.get(
                    reverse(self.path)
                )
            products_length_2 = len(response_2.context['products'])
            total_pages_2 = (
                response_2.context['pagination_range'].get('total_pages')
            )
            self.assertEqual(products_length_2, 10)
            self.assertEqual(total_pages_2, 2)

    def test_products_render_information_context_processor_in_footer(self) -> None:  # noqa: E501
        ''' create a instance of information object '''
        make_information()
        response = self.client.get(
            reverse(self.path)
        )

        self.assertEqual(response.context['information'].name,
                         'information name',
                         )
        self.assertIn('information name',
                      response.content.decode('utf-8'),
                      )

from django.test import TestCase, override_settings
from django.urls import reverse, resolve, ResolverMatch
from django.http import HttpResponse
from product import views
from product.tests.product_test_base import (
    make_category,
    make_product_range,
    make_product,
)
from unittest.mock import patch
import contextlib
import shutil


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
class ProductsFilteredByCategoryTests(TestCase):
    def setUp(self) -> None:
        self.path = 'product:category'
        return super().setUp()

    def tearDown(self) -> None:
        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)
        return super().tearDown()

    def test_product_category_url_is_correct(self) -> None:
        url: str = reverse(self.path, args=('ligamentar', ))
        self.assertEqual(url, '/produtos/ligamentar/')

    def test_product_category_loads_correct_view_func(self) -> None:
        response: ResolverMatch = resolve(
            reverse(self.path, args=('ligamentar', ))
        )
        self.assertEqual(response.func, views.product_category)

    def test_product_category_status_code_200(self) -> None:
        response: HttpResponse = self.client.get(
            reverse(self.path, args=('my-category',))
        )
        self.assertEqual(response.status_code, 200)

    def test_product_category_loads_correct_template(self) -> None:
        response: HttpResponse = self.client.get(
            reverse(self.path, args=('ligamentar', ))
        )
        self.assertTemplateUsed(response, 'product/pages/products.html')

    def test_product_category_loads_only_products_of_the_category(self) -> None:  # noqa: E501
        ''' create 4 objects in this category '''
        category_1 = make_category(name='my category', slug='my-category')
        make_product_range(4, category=category_1)

        category_2 = make_category(name='other category',
                                   slug=('other-category'),
                                   )

        ''' create 1 object in this category '''
        make_product(category=category_2,
                     name='other product',
                     slug='other-product')

        ''' make request with slug "my-category" '''
        response = self.client.get(
            reverse(self.path, args=('my-category', ))
        )

        ''' we expect 4 objects '''
        products_lenght = len(response.context['products'])

        self.assertEqual(products_lenght, 4)

    def test_products_category_page_is_paginated(self) -> None:
        ''' created 16 product objects '''
        category = make_category(name='category test', slug='category-test')
        make_product_range(16, category=category)

        path = 'product.views.PER_PAGE'

        ''' test with 4 products per page '''
        with patch(path, new=4):
            response: HttpResponse = self.client.get(
                    reverse(self.path, args=('category-test', ))
                )
            products_length = len(response.context['products'])
            total_pages = (
                response.context['pagination_range'].get('total_pages')
            )
            self.assertEqual(products_length, 4)
            self.assertEqual(total_pages, 4)

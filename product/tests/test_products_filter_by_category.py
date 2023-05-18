from django.test import TestCase, override_settings
from django.urls import reverse, resolve, ResolverMatch
from django.http import HttpResponse
from product import views
from product.tests.product_test_base import (
    make_category,
    make_product_range,
    make_product,
)
import contextlib
import shutil


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
class ProductsFilteredByCategoryTests(TestCase):
    def tearDown(self) -> None:
        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)
        return super().tearDown()

    def test_product_category_url_is_correct(self) -> None:
        url: str = reverse('product:category', args=('ligamentar', ))
        self.assertEqual(url, '/produtos/ligamentar/')

    def test_product_category_loads_correct_view_func(self) -> None:
        response: ResolverMatch = resolve(
            reverse('product:category', args=('ligamentar', ))
        )
        self.assertEqual(response.func, views.product_category)

    def test_product_category_status_code_200(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:category', args=('my-category',))
        )
        self.assertEqual(response.status_code, 200)

    def test_product_category_loads_correct_template(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:category', args=('ligamentar', ))
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
            reverse('product:category', args=('my-category', ))
        )

        ''' we expect 4 objects '''
        products_lenght = len(response.context['products'])

        self.assertEqual(products_lenght, 4)
        self.fail('testar todos os context processors '
                  'melhorar a função de formatar número do whatsapp '
                  'testar a paginação '
                  )

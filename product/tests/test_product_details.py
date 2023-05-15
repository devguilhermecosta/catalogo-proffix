from django.http import Http404, HttpResponse
from django.test import TestCase
from django.urls import ResolverMatch, resolve, reverse
from product.tests.product_test_base import make_image
from product.models import Image

from product import views

from .product_test_base import make_product


class ProductDetailsTests(TestCase):
    def setUp(self):
        make_product()
        return super().setUp()

    def test_product_details_url_is_correct(self) -> None:
        url: str = reverse('product:detail', args=('product-slug',))

        self.assertEqual(url, '/product-slug/')

    def test_product_details_load_correct_view(self) -> None:
        response: ResolverMatch = resolve(
            reverse('product:detail', args=('product-slug',))
        )
        self.assertEqual(response.func, views.product_detail)

    def test_product_details_load_correct_template(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:detail', args=('product-slug',))
        )
        self.assertTemplateUsed(response,
                                'product/pages/product_detail.html',
                                )

    def test_product_details_status_code_200(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:detail', args=('product-slug',))
        )
        self.assertEqual(response.status_code, 200)

    def test_product_detail_load_correct_data_if_product_exists(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:detail', args=('product-slug',))
        )
        content: str = response.content.decode('utf-8')

        self.assertIn('product name', content)

    def test_product_detail_load_aditional_images_if_imgs_exists(self) -> None:
        make_image(product_name='product name 2',
                   product_slug='product-slug-2')

        response: HttpResponse = self.client.get(
            reverse('product:detail', args=('product-slug-2',))
        )
        content: str = response.content.decode('utf-8')

        self.assertIn('<div class="C-detail_aditional_img">', content)
        self.assertEqual(len(Image.objects.all()), 1)

    def test_product_detail_raises_404_if_product_not_exists(self) -> None:
        response: HttpResponse = self.client.get(
            reverse('product:detail', args=('product-slug-not-exists',))
        )

        self.assertEqual(response.status_code, 404)


"""
testar a renderização de produtos não available
testar a renderização de imagens que não estão atreladas
ao produto carregado
"""

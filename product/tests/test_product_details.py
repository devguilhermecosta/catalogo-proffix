from django.http import HttpResponse
from django.test import TestCase
from django.test import override_settings
from django.urls import ResolverMatch, resolve, reverse
from product.tests.product_test_base import make_image
from product.models import Image
from product import views
from .product_test_base import make_product
import shutil
import contextlib


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
class ProductDetailsTests(TestCase):
    def setUp(self):
        make_product()

        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)
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

    def test_product_detail_returns_status_code_404_if_product_not_exists(self) -> None:  # noqa: E501
        response: HttpResponse = self.client.get(
            reverse('product:detail', args=('product-slug-not-exists',))
        )

        self.assertEqual(response.status_code, 404)

    def test_product_detail_status_code_404_if_not_available_and_method_get(self) -> None:  # noqa: E501
        make_product(name="product test", slug="product-test", available=False)
        response: HttpResponse = self.client.get(
            reverse('product:detail', args=('product-test',))
            )
        self.assertEqual(response.status_code, 404)

    def test_product_detail_load_just_images_linked_to_the_product(self):
        '''create two products objects'''
        product_1 = make_product(name="product test 1", slug="product-test-1")
        product_2 = make_product(name="product test 2", slug="product-test-2")

        '''
            create four images objects. Three images linked to the product_1,
            one image linked to the product_2.
        '''
        make_image(product=product_1)
        make_image(product=product_1)
        make_image(product=product_1)
        make_image(product=product_2)

        '''request'''
        response = self.client.get(
            reverse('product:detail', args=('product-test-1',))
        )

        content = response.content.decode('utf-8')

        self.assertIn(
            'image of product test 1',
            content,
        )
        '''
            the count is four because one of the images always
            appears twice because of the html and css modal
        '''
        self.assertContains(response, 'image of product test 1', 4)
        self.assertNotIn(
            'image of product test 2',
            content,
        )

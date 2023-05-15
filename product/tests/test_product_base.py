from django.test import TestCase, override_settings

from product.models import Category, Product, Image

from .product_test_base import (make_category, make_image, make_product,
                                make_product_range,
                                make_image_range,
                                )
import shutil
import contextlib


TEST_DIR = 'test_data'


@override_settings(MEDIA_ROOT=(TEST_DIR + '/media'))
class ProductBaseTests(TestCase):
    def tearDown(self) -> None:
        with contextlib.suppress(OSError):
            shutil.rmtree(TEST_DIR)
        return super().tearDown()

    def test_func_make_category_returs_correct_data(self) -> None:
        category = make_category()
        self.assertEqual(
            category.name,
            'this is the category'
        )
        self.assertEqual(
            category.slug,
            'this-is-the-category'
        )
        self.assertTrue(
            isinstance(category, Category)
        )

    def test_func_product_returs_correct_data(self) -> None:
        product = make_product()
        product_cover_name = product.cover.name[11:21]

        self.assertEqual(product.name, 'product name')
        self.assertEqual(product.category.name, 'this is the category')
        self.assertEqual(product_cover_name, 'image_test')
        self.assertTrue(isinstance(product, Product))

    def test_func_product_range_make_a_range_of_products(self) -> None:
        make_product_range(10)
        num_of_objects: int = len(Product.objects.all())

        self.assertEqual(num_of_objects, 10)

    def test_func_make_image_returns_a_instance_of_image(self) -> None:
        image = make_image()

        self.assertEqual(
            image.product.name, 'product name'
        )
        self.assertEqual(
            image.cover.name[22:32], 'image_test',
        )
        self.assertTrue(isinstance(image, Image))

    def test_func_make_image_range_returns_a_range_of_image(self) -> None:
        make_image_range(5)
        num_of_images: int = len(Image.objects.all())

        self.assertEqual(num_of_images, 5)

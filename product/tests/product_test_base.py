from product.models import Product, Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from .base_exception import ImageNotFoundError
from pathlib import Path
from decimal import Decimal


def __create_simple_image() -> SimpleUploadedFile:
    try:
        path: Path = Path(__file__).parent.parent.parent
        image_path: str = ''.join(
            [str(path), '/utils/tests/images/image_test.jpeg']
            )
        simple_image: SimpleUploadedFile = SimpleUploadedFile(
            name='image_test',
            content=open(image_path, 'rb').read(),
            content_type='image/jpeg',
            )
    except FileNotFoundError:
        raise ImageNotFoundError('Image not Found')
    return simple_image


def make_category(**kwargs) -> Category:
    """optional params:

        name, slug

    Returns:
        Category object
    """
    category_data: dict = {
        'name': kwargs.pop('name', 'this is the category'),
        'slug': kwargs.pop('slug', 'this-is-the-category'),
    }
    category = Category.objects.create(**category_data)

    return category


def make_product(category=None, **kwargs) -> Product:
    """function for create a instance of Product

    Args:
        category = optional instance of category,
        optional kwargs = name, slug, description, available, price

    Returns:
        Product
    """
    product_data: dict = {
        'name': kwargs.pop('name', 'product name'),
        'category': category if category is not None else make_category(),
        'slug': kwargs.pop('slug', 'product-slug'),
        'cover': __create_simple_image(),
        'description': kwargs.pop('description', 'product description'),
        'price': kwargs.pop('price', Decimal(0.0)),
        'available': kwargs.pop('available', True),
    }
    new_product = Product.objects.create(**product_data)
    new_product.save()

    return new_product


def make_product_range(number_of_objects: int, category=None):
    """make a range of Product objects

    Args:
        number_of_objects (int): number of need objects
    Optional kwargs:
        category: Instance of Category
    """
    for i in range(number_of_objects):
        make_product(
            category=category if category is not None else category,
            name=f'name of product {i}',
            slug=f'slug-of-product-{i}',
            description=f'description-of-product-{i}'
        )


def make_image(product=None, **kwargs) -> Image:
    """
        optional: product_name, product_slug
    """
    image_data: dict = {
        'product': make_product(
            category=kwargs.pop('category', None),
            name=kwargs.pop('product_name', 'product name'),
            slug=kwargs.pop('product_slug', 'product-slug')
            ) if product is None else product,
        'cover': __create_simple_image()
    }
    new_image = Image.objects.create(**image_data)

    return new_image


def make_image_range(number_of_objects) -> None:
    """make a range of Image objects

    Args:
        number_of_objects (int): number of need objects
    """
    for i in range(number_of_objects):
        make_image(
            product_name=f'product-name-{i}',
            product_slug=f'product-slug-{i}',
            )

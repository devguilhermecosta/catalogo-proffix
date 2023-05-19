from django.db import models
from django.utils.text import slugify
from django.conf import settings
from PIL import Image as Imgpil
import os


def resize_image(full_path: str, new_width: int = 920) -> None:
    image_conversion = Imgpil.open(full_path)
    original_w, original_h = image_conversion.size

    if original_w < new_width:
        image_conversion.close()
        return

    new_height: int = round((new_width * original_h) / original_w)
    new_image = image_conversion.resize(
        (new_width, new_height),
        resample=Image.Resampling.LANCZOS,
        )
    new_image.save(
        full_path,
        optimize=True,
        quality=60,
    )


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='nome')
    slug = models.CharField(max_length=60)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'


class Product(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name='nome',
                            unique=True,
                            )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='categoria',
                                 )
    slug = models.CharField(max_length=255,
                            unique=True,
                            default='',
                            )
    cover = models.ImageField(upload_to='images-products/',
                              blank=True,
                              null=True,
                              verbose_name='imagem de apresentação',
                              )
    description = models.TextField(verbose_name='descrição')
    available = models.BooleanField(default=True,
                                    verbose_name='disponível')

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(self.name)

        if self.cover:
            image_name: str = self.cover.name
            full_path: str = os.path.join(settings.MEDIA_ROOT, image_name)
            resize_image(full_path)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='images-products/',
                              blank=True,
                              null=True,
                              verbose_name='imagens do produto'
                              )

    def __str__(self):
        return self.cover.name

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)

        if self.cover:
            image_name: str = self.cover.name
            full_path: str = os.path.join(settings.MEDIA_ROOT, image_name)
            resize_image(full_path)

    class Meta:
        verbose_name = 'imagem'
        verbose_name_plural = 'imagens'

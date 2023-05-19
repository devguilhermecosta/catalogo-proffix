from django.db import models
from django.utils.text import slugify


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

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

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

    class Meta:
        verbose_name = 'imagem'
        verbose_name_plural = 'imagens'

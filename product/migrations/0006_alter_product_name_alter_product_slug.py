# Generated by Django 4.2.1 on 2023-05-13 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_product_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]

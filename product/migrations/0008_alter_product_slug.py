# Generated by Django 4.2.1 on 2023-05-13 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
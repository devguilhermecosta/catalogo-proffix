# Generated by Django 4.2.1 on 2023-05-17 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0002_alter_information_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docs',
            name='afe',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
        migrations.AlterField(
            model_name='docs',
            name='cnpj',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
        migrations.AlterField(
            model_name='docs',
            name='crt',
            field=models.FileField(blank=True, null=True, upload_to='docs/'),
        ),
    ]
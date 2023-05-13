# Generated by Django 4.2.1 on 2023-05-13 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50, verbose_name='telefone')),
                ('fax', models.CharField(max_length=50)),
                ('whatsapp', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('about', models.TextField(verbose_name='sobre a empresa')),
            ],
            options={
                'verbose_name': 'informação',
                'verbose_name_plural': 'informações',
            },
        ),
        migrations.CreateModel(
            name='Docs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('afe', models.FileField(blank=True, null=True, upload_to='media/docs/')),
                ('cnpj', models.FileField(blank=True, null=True, upload_to='media/docs/')),
                ('crt', models.FileField(blank=True, null=True, upload_to='media/docs/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='information.information')),
            ],
            options={
                'verbose_name': 'documento',
                'verbose_name_plural': 'documentos',
            },
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-04 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_has_sizes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-17 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_category_product_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='product',
            new_name='product_id',
        ),
    ]
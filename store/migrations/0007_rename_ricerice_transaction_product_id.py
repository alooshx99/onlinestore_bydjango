# Generated by Django 5.1.1 on 2024-09-17 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_rename_product_id_transaction_ricerice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='ricerice',
            new_name='product_id',
        ),
    ]

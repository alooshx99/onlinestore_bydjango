# Generated by Django 5.1.1 on 2024-09-17 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_transaction_total_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='product_id',
            new_name='ricerice',
        ),
    ]

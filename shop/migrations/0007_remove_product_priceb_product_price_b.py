# Generated by Django 4.1.5 on 2023-04-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_product_priceb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='priceb',
        ),
        migrations.AddField(
            model_name='product',
            name='price_b',
            field=models.FloatField(default=16),
            preserve_default=False,
        ),
    ]

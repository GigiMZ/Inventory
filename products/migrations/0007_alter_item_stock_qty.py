# Generated by Django 5.1.6 on 2025-03-26 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_item_stock_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock_qty',
            field=models.PositiveIntegerField(default=0),
        ),
    ]

# Generated by Django 5.1.6 on 2025-03-29 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
        ('products', '0007_alter_item_stock_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_items', to='products.item')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_items', to='locations.location')),
            ],
        ),
    ]

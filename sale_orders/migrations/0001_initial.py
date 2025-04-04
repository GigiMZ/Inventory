# Generated by Django 5.1.6 on 2025-03-15 14:25

import django.db.models.deletion
import sale_orders.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0005_alter_category_archived_alter_item_archived'),
    ]

    operations = [
        migrations.CreateModel(
            name='SaleOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('write_date', models.DateTimeField(auto_now=True)),
                ('archived', models.BooleanField(default=False, editable=False)),
                ('name', models.CharField(default=sale_orders.models.generate_name, editable=False, max_length=7)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SaleOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('write_date', models.DateTimeField(auto_now=True)),
                ('archived', models.BooleanField(default=False, editable=False)),
                ('qty', models.PositiveIntegerField(default=0)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_items', to='products.item')),
                ('sale_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sale_items', to='sale_orders.saleorder')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

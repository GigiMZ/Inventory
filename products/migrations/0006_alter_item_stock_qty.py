# Generated by Django 5.1.6 on 2025-03-22 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_category_archived_alter_item_archived'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='stock_qty',
            field=models.IntegerField(default=0),
        ),
    ]

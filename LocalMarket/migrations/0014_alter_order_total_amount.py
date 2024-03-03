# Generated by Django 4.2.10 on 2024-03-03 00:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocalMarket', '0013_alter_orderitem_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.FloatField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]

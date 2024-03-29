# Generated by Django 4.2.10 on 2024-03-02 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LocalMarket', '0008_customer_city_customer_zip_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_name',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('food_bevarages', 'Food and Bevarages'), ('fruits_veg', 'Fruits and Vegetables'), ('dairy', 'Dairy'), ('other', 'Other')], default=None, max_length=14),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('Cancelled', 'Cancelled'), ('Placed', 'Placed'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Ongoing', max_length=9),
        ),
    ]

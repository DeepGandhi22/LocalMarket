# Generated by Django 4.2.10 on 2024-03-02 23:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0004_alter_shop_gst_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_city',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_zip_code',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_address',
            field=models.CharField(default=None, max_length=200),
        ),
    ]

# Generated by Django 3.1.7 on 2021-03-12 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('click2buy', '0003_order_orderitem_reviews_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
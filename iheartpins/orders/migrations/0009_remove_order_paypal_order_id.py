# Generated by Django 3.2.4 on 2021-07-06 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210705_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paypal_order_id',
        ),
    ]

# Generated by Django 3.2.4 on 2021-07-01 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='buyer_name',
        ),
        migrations.AddField(
            model_name='order',
            name='buyer_firstname',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='buyer_lastname',
            field=models.CharField(default='test', max_length=255),
            preserve_default=False,
        ),
    ]

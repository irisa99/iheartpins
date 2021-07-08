# Generated by Django 3.2.4 on 2021-07-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20210701_0244'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='billing_status',
            new_name='paid',
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='payout_complete',
            field=models.BooleanField(default=False),
        ),
    ]

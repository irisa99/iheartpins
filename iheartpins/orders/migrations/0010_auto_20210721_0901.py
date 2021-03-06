# Generated by Django 3.2.5 on 2021-07-21 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trans', '0001_initial'),
        ('orders', '0009_remove_order_paypal_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='listing',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderitem', to='trans.listing'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='seller_payout',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]

# Generated by Django 3.2.4 on 2021-06-28 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210627_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tradecredits',
            name='credit',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 3.2.4 on 2021-06-29 04:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210628_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='accounts.person'),
        ),
        migrations.AlterField(
            model_name='person',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='name', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]

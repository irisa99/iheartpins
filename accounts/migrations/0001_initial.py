# Generated by Django 3.2.4 on 2021-06-24 03:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(max_length=30, unique=True)),
                ('user_date_created', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('user_last_edit', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last edit')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser')),
                ('is_admin', models.BooleanField(default=False, verbose_name='administrator')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff')),
                ('user_type', models.CharField(blank=True, max_length=60, null=True)),
                ('user_status', models.CharField(blank=True, max_length=60, null=True)),
                ('warning_flag', models.CharField(blank=True, max_length=60, null=True)),
                ('uom_pref', models.CharField(blank=True, max_length=30, null=True)),
                ('bal_trade_credits', models.IntegerField(blank=True, null=True)),
                ('current_rating', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('user_notes', models.TextField(blank=True, null=True)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TradeCredits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts.user')),
            ],
        ),
    ]
# Generated by Django 4.2.5 on 2023-09-07 13:22

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_trade_stream', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='btcusd',
            name='symbol',
        ),
        migrations.RemoveField(
            model_name='solusd',
            name='symbol',
        ),
        migrations.RemoveField(
            model_name='xrpusd',
            name='symbol',
        ),
        migrations.AddField(
            model_name='btcusd',
            name='received_time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 9, 7, 13, 22, 5, 196788, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solusd',
            name='received_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='xrpusd',
            name='received_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
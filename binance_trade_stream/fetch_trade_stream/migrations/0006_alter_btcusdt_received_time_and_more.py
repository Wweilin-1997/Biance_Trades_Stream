# Generated by Django 4.2.5 on 2023-09-12 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch_trade_stream', '0005_alter_btcusdt_price_alter_solusdt_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='btcusdt',
            name='received_time',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='solusdt',
            name='received_time',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='xrpusdt',
            name='received_time',
            field=models.BigIntegerField(),
        ),
    ]
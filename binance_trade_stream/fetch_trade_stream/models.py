from django.db import models

# Create your models here.

class BTCUSDT(models.Model) :
    event_time = models.BigIntegerField()
    trade_id = models.BigIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=8)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    buyer_trade_id = models.IntegerField()
    seller_trade_id = models.IntegerField()
    trade_time = models.BigIntegerField()
    buyer_mm = models.BooleanField()
    received_time= models.BigIntegerField()


class XRPUSDT(models.Model) :
    event_time = models.BigIntegerField()
    trade_id = models.BigIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=8)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    buyer_trade_id = models.IntegerField()
    seller_trade_id = models.IntegerField()
    trade_time = models.BigIntegerField()
    buyer_mm = models.BooleanField()
    received_time= models.BigIntegerField()

class SOLUSDT(models.Model) :
    event_time = models.BigIntegerField()
    trade_id = models.BigIntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=8)
    quantity = models.DecimalField(max_digits=20, decimal_places=8)
    buyer_trade_id = models.IntegerField()
    seller_trade_id = models.IntegerField()
    trade_time = models.BigIntegerField()
    buyer_mm = models.BooleanField()
    received_time= models.BigIntegerField()
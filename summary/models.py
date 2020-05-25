import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class PreviousClose(models.Model):
    # previous_close = models.CharField(max_length=50)
    previous_close = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField()

    def __str__(self):
        return self.previous_close

    def findinig_date(self):
        self.date = timezone.now() - datetime.timedelta(days=1)

class OpenPrice(models.Model):
    open_price = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.open_price

class EnterpriseValue(models.Model):
    enterprise_value = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.enterprise_value

class MarketCap(models.Model):
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.market_cap

class EarningsPerShare(models.Model):
    eps = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.eps

class PriceToEarnings(models.Model):
    pe_reatio = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return self.pe_reatio
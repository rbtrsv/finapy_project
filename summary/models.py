import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class PreviousClose(models.Model):
    # previous_close = models.CharField(max_length=50)
    previous_close = models.DecimalField(max_digits=200, decimal_places=2)
    date = models.DateTimeField()

    def __str__(self):
        return self.previous_close

    def findinig_date(self):
        self.date = timezone.now() - datetime.timedelta(days=1)

class OpenPrice(models.Model):
    open_price = models.DecimalField(max_digits=200, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.open_price

class EnterpriseValue(models.Model):
    enterprise_value = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return self.enterprise_value

class MarketCap(models.Model):
    market_cap = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return self.market_cap

class EarningsPerShare(models.Model):
    eps = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return self.eps

class PriceToEarnings(models.Model):
    pe_ratio = models.DecimalField(max_digits=200, decimal_places=2)

    def __str__(self):
        return self.pe_ratio

class Stock(models.Model):
    stock_name = models.CharField(max_length=50)
    stock_ticker = models.CharField(max_length=5)
    stock_description = models.TextField(max_length=5000)
    price_date = models.DateTimeField('price date')

    previous_close = models.ForeignKey('PreviousClose', on_delete=models.CASCADE)
    open_price =  models.ForeignKey('OpenPrice', on_delete=models.CASCADE)
    enterprise_value =  models.ForeignKey('EnterpriseValue', on_delete=models.CASCADE)
    market_cap = models.ForeignKey('MarketCap', on_delete=models.CASCADE)
    eps = models.ForeignKey('EarningsPerShare', on_delete=models.CASCADE)
    pe_ratio =  models.ForeignKey('PriceToEarnings', on_delete=models.CASCADE)

    def __str__(self):
        return self.stock_name

import uuid # Required for unique stock instances
from django.contrib.auth.models import User

class StockInstance(models.Model):
    """Model representing a specific stock (i.e. that has been bought by a client)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, help_text='Unique ID for this particular stock across whole platform')
    stock = models.ForeignKey('Stock', on_delete=models.SET_NULL, null=True)
    # "blank=True" if you wish to permit empty values in forms. Here there is no owner of the stock.
    client = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    INSTANCE_STATUS = (
            ('a', 'Available'),
            ('b', 'Borrowed'),
        )

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.stock.stock_name})'
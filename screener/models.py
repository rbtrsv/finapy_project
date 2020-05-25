from django.db import models
from django.utils import timezone

# Create your models here.
class Stock(models.Model):
    stock_name = models.CharField(max_length=50)
    price_date = models.DateTimeField('price date')

    def __str__(self):
        return self.stock_name
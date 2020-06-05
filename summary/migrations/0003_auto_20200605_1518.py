# Generated by Django 3.0.6 on 2020-06-05 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0002_auto_20200527_1200'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'ordering': ['stock_halt'], 'permissions': (('can_mark_trading_halt', 'Set trading as halted'),)},
        ),
        migrations.AddField(
            model_name='stock',
            name='stock_halt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='stock',
            name='price_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
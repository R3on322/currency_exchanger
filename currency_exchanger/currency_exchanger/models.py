from django.db import models


class Currency(models.Model):

    ValueId = models.CharField(max_length=500)
    CurrencyValue = models.FloatField(max_length=500)
    LastUpdDate = models.IntegerField()

    class Meta:
        db_table = 'Currency'
        managed = True
        verbose_name = 'Currency'

    # {'success': True, 'timestamp': 1658314144, 'base': 'USD', 'date': '2022-07-20',
    #  'rates': {'BTC': 4.2305139e-05, 'EUR': 0.982045, 'USD': 1, 'BRL': 5.414199, 'ETH': 1579.43}}
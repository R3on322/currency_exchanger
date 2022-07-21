from django.db import models

class Currency(models.Model):

    success = models.BooleanField()
    def_currency = models.CharField(max_length=5)
    last_upd_date = models.CharField(max_length=10)
    currency_values = models.CharField(max_length=255)

    # {'success': True, 'timestamp': 1658314144, 'base': 'USD', 'date': '2022-07-20',
    #  'rates': {'BTC': 4.2305139e-05, 'EUR': 0.982045, 'USD': 1, 'BRL': 5.414199, 'ETH': 1579.43}}

    class Meta:
        managed = True
        verbose_name = 'Currency'


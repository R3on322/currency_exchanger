from django.db import models


class Currency(models.Model):

    CurrencyId = models.AutoField(primary_key=True)
    LastUpdDate = models.DateTimeField(max_length=500)
    Value = models.ForeignKey(
        'Value',
        on_delete=models.CASCADE
    )

    class Meta:
        managed = True
        verbose_name = 'Currency'


class Value(models.Model):

    ValueId = models.AutoField(primary_key=True)
    USD = models.IntegerField()
    EUR = models.IntegerField()
    ETH = models.IntegerField()
    BTC = models.IntegerField()
    BRL = models.IntegerField()


    class Meta:
        managed = True
        verbose_name = 'Valuer'

    # {'success': True, 'timestamp': 1658314144, 'base': 'USD', 'date': '2022-07-20',
    #  'rates': {'BTC': 4.2305139e-05, 'EUR': 0.982045, 'USD': 1, 'BRL': 5.414199, 'ETH': 1579.43}}


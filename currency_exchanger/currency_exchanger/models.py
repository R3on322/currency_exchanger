from django.db import models


class Currency(models.Model):

    ValueId = models.CharField(max_length=500, unique=True, primary_key=True)
    CurrencyValue = models.FloatField(max_length=500)
    LastUpdDate = models.CharField(max_length=100)

    class Meta:
        db_table = 'Currency'
        managed = True
        verbose_name = 'Currency'

    def __str__(self):
        return f'{self.ValueId} {self.CurrencyValue}'

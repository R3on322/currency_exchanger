from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.Serializer):
    currency_values = serializers.CharField()

    class Meta:
        managed = True
        verbose_name = 'Currency'

# {
#  "sourceValue" : 123.45,
#  "resultValue" : 126919856183,
#  "sourceCurrency" : "BTC",
#  "resultCurrency" : "EUR"
# }
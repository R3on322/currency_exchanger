from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['last_upd_date', 'currency_values']

class ExchangerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['count_cur','result_cur', 'def_currency']


# {
#  "sourceValue" : 123.45,
#  "resultValue" : 126919856183,
#  "sourceCurrency" : "BTC",
#  "resultCurrency" : "EUR"
# }
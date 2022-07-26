from rest_framework import serializers
from .models import Currency


class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ['last_upd_date', 'currency_values']

class ExchangerModel:
    def __init__(self, count_cur, result_cur):
        self.count_cur = count_cur
        self.result_cur = result_cur

class ExchangerSerializer(serializers.Serializer):
    count_cur = serializers.IntegerField(max_value=5)
    result_cur = serializers.CharField(max_length=10)

#  "sourceValue" : 123.45,
#  "resultValue" : 126919856183,
#  "sourceCurrency" : "BTC",
#  "resultCurrency" : "EUR"
# }
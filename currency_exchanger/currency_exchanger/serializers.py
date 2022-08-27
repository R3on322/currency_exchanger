from rest_framework import serializers
from .models import Currency


class CurrencyViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('ValueId', 'CurrencyValue', 'LastUpdDate')


class ExchangerSerializer(serializers.Serializer):

    count_currency = serializers.IntegerField(min_value=1)
    result_currency = serializers.CharField()

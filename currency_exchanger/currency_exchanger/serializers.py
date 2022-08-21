from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Currency


class ExchangerSerializer(serializers.Serializer):
    count_cur = serializers.IntegerField()
    result_cur = serializers.CharField()

class CurrencyViewSerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = ('ValueId', 'CurrencyValue')


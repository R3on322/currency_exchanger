from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Currency


class CurrencyViewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('ValueId', 'CurrencyValue', 'LastUpdDate')


class ExchangerSerializer(serializers.Serializer):

    count_currency = serializers.IntegerField(min_value=1)
    result_currency = serializers.CharField()

    def validate_result_currency(self, value):
        if value not in list(Currency.objects.values_list('ValueId', flat=True)):
            raise ValidationError('Wrong Value')
        return value

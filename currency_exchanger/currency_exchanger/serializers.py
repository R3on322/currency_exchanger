from rest_framework import serializers
from .models import Currency


class ExchangerModel:
    def __init__(self, count_cur, result_cur):
        self.count_cur = count_cur
        self.result_cur = result_cur

class ExchangerSerializer(serializers.Serializer):
    count_cur = serializers.IntegerField()
    result_cur = serializers.CharField()


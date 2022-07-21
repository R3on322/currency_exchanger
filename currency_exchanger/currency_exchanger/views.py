from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from currency_exchanger.request import request as request_currency
from .models import Currency
from .secrets import API_TOKEN, BASE_CURRENCY_URL
from .serializers import CurrencySerializer
# from .exchanger_api import Exchanger

# data_base = {'success': True, 'timestamp': 1658320863, 'base': 'USD', 'date': '2022-07-20',
#              'rates': {'BTC': 4.2338501e-05, 'EUR': 0.980695, 'USD': 1, 'BRL': 5.441598, 'ETH': 1589.04}}


class CurrencyView(APIView):

    def get(self, request):
        queryset = Currency.objects.all()
        return Response({'Currencies': CurrencySerializer(queryset, many=True).data})

    # def post(self, request):
    #     pass

from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Currency
from .serializers import CurrencySerializer, ExchangerSerializer
from .exchanger_api import Exchanger


class CurrencyView(generics.ListAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class ExchangerAPI(APIView):

    def post(self, request):
        serializer = ExchangerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        exchanger_response = Exchanger(serializer)
        return Response(exchanger_response)

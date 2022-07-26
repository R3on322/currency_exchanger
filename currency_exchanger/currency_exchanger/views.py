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
        if serializer.is_valid():
            count_cur = request.data.get('count_cur')
            result_cur = request.data.get('result_cur')
            result = Exchanger(count_cur, result_cur)
            return Response(f'result: {result}')
        return Response(serializer.errors)


# POST response in browser:
{
"count_cur": 2,
"result_cur": "EUR"
}
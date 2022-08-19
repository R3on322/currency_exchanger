from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .serializers import ExchangerSerializer, CurrencyViewSerializer
from .exchanger_api import Exchanger
from .requests_to_db import RequestToDB
from currency_exchanger.models import Currency

class CurrencyView(ModelViewSet):
    # RequestToDB().data_update()
    queryset = Currency.objects.all()
    serializer_class = CurrencyViewSerializer

class ExchangerAPI(APIView):

    def post(self, request):
        # RequestToDB().data_update()
        serializer = ExchangerSerializer(data=request.data)
        if serializer.is_valid():
            count_cur = request.data.get('count_cur')
            result_cur = request.data.get('result_cur').upper()
            val_currency = RequestToDB().currencyfromdb()[result_cur]
            result = Exchanger(count_cur, result_cur, val_currency)
            return Response(str(result))
        return Response(serializer.errors)


# POST response in browser:
{
"count_cur": 2,
"result_cur": "EUR"
}
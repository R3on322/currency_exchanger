from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ExchangerSerializer
from .exchanger_api import Exchanger
from .requests_to_db import RequestToDB


class CurrencyView(APIView):

    def get(self, request):
        RequestToDB().data_update()
        currency_list = RequestToDB().currencyfromdb()
        #date = RequestToDB().datefromdb()             # need to fix
        return Response({"date": currency_list})


class ExchangerAPI(APIView):

    def post(self, request):
        RequestToDB().data_update()
        serializer = ExchangerSerializer(data=request.data)
        if serializer.is_valid():
            count_cur = request.data.get('count_cur')
            result_cur = request.data.get('result_cur').upper()
            result = Exchanger(count_cur, result_cur)
            return Response(f'Result: {result}')
        return Response(serializer.errors)


# POST response in browser:
{
"count_cur": 2,
"result_cur": "EUR"
}
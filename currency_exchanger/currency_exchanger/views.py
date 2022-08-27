from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from currency_exchanger.models import Currency
from currency_exchanger.request import request as course_data
from currency_exchanger.secrets import API_TOKEN, BASE_CURRENCY_URL
from .serializers import ExchangerSerializer, CurrencyViewSerializer
from .exchanger_api import Exchanger


class CurrencyView(ReadOnlyModelViewSet):
    # RequestToDB().data_update()
    queryset = Currency.objects.all()
    serializer_class = CurrencyViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ExchangerAPI(APIView):

    def post(self, request):
        # RequestToDB().data_update()
        serializer = ExchangerSerializer(data=request.data)
        if serializer.is_valid():
            count_cur = request.data.get('count_currency')
            result_cur = request.data.get('result_currency').upper()
            val_currency = (Currency.objects.filter(ValueId=result_cur).values('CurrencyValue'))[0]['CurrencyValue']
            result = Exchanger(count_cur, result_cur, val_currency)
            return Response(str(result))
        return Response(serializer.errors)


# POST response in browser:
{
"count_currency": 1000,
"result_currency": "EUR"
}
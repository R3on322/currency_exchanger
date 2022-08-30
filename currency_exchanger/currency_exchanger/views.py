from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from currency_exchanger.models import Currency
from .serializers import ExchangerSerializer, CurrencyViewSerializer
from .exchanger_api import Exchanger


class CurrencyView(ReadOnlyModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencyViewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ExchangerAPI(APIView):

    def post(self, request):
        serializer = ExchangerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        count_cur = serializer.validated_data['count_currency']
        result_cur = serializer.validated_data['result_currency'].upper()
        val_currency = (Currency.objects.filter(ValueId=result_cur).values('CurrencyValue'))[0]['CurrencyValue']
        result = Exchanger(count_cur, result_cur, val_currency)
        return Response(str(result))

# POST response in browser:
{
    "count_currency": 1000,
    "result_currency": "EUR"
}
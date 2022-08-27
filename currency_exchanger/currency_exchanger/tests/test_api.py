from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from currency_exchanger.models import Currency
from currency_exchanger.serializers import CurrencyViewSerializer


class ExchangerAPITestCase(APITestCase):

    def test_get(self):
        currency_val_1 = Currency.objects.create(ValueId="EUR", CurrencyValue=0.93, LastUpdDate=1808)
        currency_val_2 = Currency.objects.create(ValueId="ASD", CurrencyValue=10, LastUpdDate=2208)
        url = reverse('currency_page')
        response = self.client.get(url)
        serializer_data = CurrencyViewSerializer([currency_val_1, currency_val_2], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

#need to do
    # def test_post(self):
    #     pass

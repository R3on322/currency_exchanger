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

    def test_post(self):
        Currency.objects.create(ValueId="EUR", CurrencyValue=0.93, LastUpdDate=1808)
        url = reverse('currency_exchanger')
        response = self.client.post(url, {"count_currency": 1000, "result_currency": "EUR"})
        expected_data = "Source Currency: USD, Source Value: 1000, Result Currency: EUR, Result Value: 930.0"
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(expected_data, response.data)

    def test_post_bad_request(self):
        Currency.objects.create(ValueId="EUR", CurrencyValue=0.93, LastUpdDate=1808)
        Currency.objects.create(ValueId="ASD", CurrencyValue=10, LastUpdDate=2208)
        url = reverse('currency_exchanger')
        response = self.client.post(url, {'BTC': 'asd'})
        expected_data = {'count_currency': ['This field is required.'],
                         'result_currency' : ['This field is required.']}
        self.assertEqual(expected_data, response.json())

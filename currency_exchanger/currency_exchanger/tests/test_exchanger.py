from django.test import TestCase

from currency_exchanger.exchanger_api import Exchanger


class ExchangerTestCase(TestCase):

    def test_exchanger(self):
        result = Exchanger(10, 'EUR', 0.9820)
        expected_data = "Source Currency: USD, Source Value: 10, Result Currency: EUR, Result Value: 9.82"
        self.assertEqual(expected_data, str(result))

    def test_exchanger_less_zero(self):
        result = Exchanger(-100000, 'BTC', 4.0526988e-05)
        expected_data = "Source Currency: USD, Source Value: -100000, Result Currency: BTC, Result Value: Value Error"
        self.assertEqual(expected_data, str(result))

    def test_exchanger_other_currency(self):
        result = Exchanger(16, 'RUB', 10)
        expected_data = "Source Currency: USD, Source Value: 16, Result Currency: RUB, Result Value: Error! Currency not in list..."
        self.assertEqual(expected_data, str(result))
from django.test import TestCase

from currency_exchanger.exchanger_api import Exchanger


class ExchangerTestCase(TestCase):

    def test_exchanger(self):
        result = Exchanger(10, 'EUR', 0.9820)
        expected_data = "Source Currency: USD, Source Value: 10, Result Currency: EUR, Result Value: 9.82"
        self.assertEqual(expected_data, str(result))

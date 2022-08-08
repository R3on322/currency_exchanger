from .requests_to_db import RequestToDB


class Exchanger:

    def __init__(self, count, currency, def_value = 1, def_currency = 'USD'):
        self.def_val = def_value
        self.def_currency = def_currency
        self.count = count
        self.currency = currency
        self.val_currency = RequestToDB().currencyfromdb()[currency]
        self.res_exch = self.exchanger()

    def exchanger(self) -> float:
        self.res_exch = round((self.def_val * self.val_currency), 5) * self.count
        return self.res_exch

    def __repr__(self):
        return f'Source Currency: {self.def_currency}, Source Value: {self.count}, Result Currency: {self.currency}, Result Value: {self.res_exch} '
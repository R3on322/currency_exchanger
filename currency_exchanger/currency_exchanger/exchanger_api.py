class Exchanger:

    def __init__(self, count, currency, val_currency, def_value=1, def_currency='USD'):
        self.count = count
        self.currency = currency
        self.val_currency = val_currency
        self.def_val = def_value
        self.def_currency = def_currency
        self.res_exch = self.exchanger()

    def exchanger(self) -> float:
        self.res_exch = (self.def_val * self.val_currency) * float(self.count)
        return self.res_exch

    def __repr__(self):
        return f'Source Currency: {self.def_currency}, ' \
               f'Source Value: {self.count}, ' \
               f'Result Currency: {self.currency}, ' \
               f'Result Value: {self.res_exch}'

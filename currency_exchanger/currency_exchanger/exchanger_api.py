from .models import Currency


class Exchanger:
    crypto_curr_list = ['ETH']

    def __init__(self, count, currency, def_value = 1, def_currency = 'USD'):
        self.def_val = def_value
        self.def_currency = def_currency
        self.count = count
        self.currency = currency
        self.val_currency = to_dict_currency[currency]
        self.res_exch = self.exchanger()

    def exchanger(self) -> float:
        if self.currency in self.crypto_curr_list:
            self.res_exch = round((self.def_val / self.val_currency), 5) * self.count
        else:
            self.res_exch = round((self.def_val * self.val_currency), 5) * self.count
        return self.res_exch

    def __repr__(self):
        return f'{self.def_currency}({self.count}) -> {self.currency}({self.res_exch})'


data_base = Currency.objects.all()
currency_from_base = data_base[0].currency_values.strip("{}")
to_dict_currency = dict((currency.replace("'","").lstrip(" "), float(value)) for currency, value in (string_cur.split(':') for string_cur in currency_from_base.split(',')))
# print(Exchanger(2, "ETH"))
class Exchanger:

    def __init__(self, count, currency, val_currency, def_value = 1, def_currency = 'USD'):
        self.count = count
        self.currency = currency
        self.val_currency = val_currency
        self.def_val = def_value
        self.def_currency = def_currency
        self.res_exch = self.exchanger()

    def exchanger(self) -> float:
        try:
            if self.count < 0:
                raise ValueError
            elif self.currency not in ["ASD", "BTC", "EUR", "USD"]:
                raise NameError
            self.res_exch = round((self.def_val * self.val_currency), 5) * self.count
            return self.res_exch
        except ValueError:
            return "Value Error"
        except NameError:
            return "Error! Currency not in list..."

    def __repr__(self):
        return f'Source Currency: {self.def_currency}, Source Value: {self.count}, Result Currency: {self.currency}, Result Value: {self.res_exch}'
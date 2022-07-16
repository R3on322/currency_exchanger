from request import result

# result = {
#     "success": True,
#     "timestamp": 1657961703,
#     "base": "USD",
#     "date": "2022-07-16",
#     "rates": {
#         "USD": 1,
#         "BRL": 5.407804,
#         "EUR": 0.99138,
#         "BTC": 4.8570222e-05
#     }
# }

class Exchanger:

    def __init__(self, count, currency, def_value = 1, def_currency = result['base']):
        self.def_val = def_value
        self.def_currency = def_currency
        self.count = count
        self.currency = currency
        self.num_currency = result['rates'][currency]
        self.res_exch = self.exchanger()


    def exchanger(self) -> float:
        self.res_exch = (self.def_val * self.num_currency) * self.count
        return self.res_exch

    def __repr__(self):
        return f'{self.def_currency} -> {self.currency} = {self.res_exch}'



rates_names = ', '.join([i for i in result['rates'].keys()])

while True:
    try:
        currency = str(input('Input currency: ').upper())
        count = int(input('Input count of currency: '))
        if currency not in rates_names:
            raise NameError
        else:
            break

    except ValueError:
        print('Error! Chek type of count and currency(count = numbers, currency = letters)')

    except NameError:
        print(f'Error! Chek name of currency({rates_names})')

exchngr = Exchanger(count, currency)
print(exchngr)



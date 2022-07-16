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

    def __init__(self, def_value = 1, def_currency = result['base']):
        self.def_val = def_value
        self.def_currency = def_currency

    def exchanger(self, count, currency):
        try:
            count = int(count)
            int_currency = float(result['rates'][currency])
        except ValueError:
            print('Error! Chek type of count and currency(chek = int, currency = str)')

        result_exch = (self.def_val * int_currency) * count

        return f'{self.def_currency} -> {currency} = {result_exch}'


currency = str(input('Input currency: ').upper())
count = int(input('Input count of currency: '))
exchngr = Exchanger()
print(exchngr.exchanger(count, currency))



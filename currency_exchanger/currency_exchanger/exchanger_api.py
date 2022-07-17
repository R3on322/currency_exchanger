from request import request
import secrets


request_result = request(secrets.API_TOKEN, secrets.BASE_CURRENCY_URL)
rates_names = ' '.join([i for i in request_result['rates'].keys()])

class Exchanger:

    def __init__(self, count, currency, def_value = 1, def_currency = request_result['base']):
        self.def_val = def_value
        self.def_currency = def_currency
        self.count = count
        self.currency = currency
        self.num_currency = request_result['rates'][currency]
        self.res_exch = self.exchanger()

    def exchanger(self) -> float:
        self.res_exch = (self.def_val * self.num_currency) * self.count
        return self.res_exch

    def __repr__(self):
        return f'{self.def_currency} -> {self.currency} = {self.res_exch}'


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
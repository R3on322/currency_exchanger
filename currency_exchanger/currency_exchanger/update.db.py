import psycopg2
from request import request
from .secrets import API_TOKEN, BASE_CURRENCY_URL, URL_FOR_ETH


def data_update(request):
    conn = psycopg2.connect(host='127.0.0.1', user='postgres', password='newdb1337', dbname='currencydb')
    for ValueId, CurrencyValue in request['rates'].items():
         cur = conn.cursor()
         cur.execute("""UPDATE public."Value" SET "CurrencyValue" = {} WHERE "ValueId" = '{}'""".format(CurrencyValue,ValueId))
         conn.commit()
    cur.close()
    conn.close()
    return

data_update(request(API_TOKEN,BASE_CURRENCY_URL))




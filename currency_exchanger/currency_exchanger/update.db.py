import psycopg2
import schedule
from request import request
from .secrets import API_TOKEN, BASE_CURRENCY_URL, URL_FOR_ETH


def data_update():
    conn = psycopg2.connect(host='127.0.0.1', user='postgres', password='newdb1337', dbname='currencydb')
    request_for_db = request(API_TOKEN, BASE_CURRENCY_URL)
    for ValueId, CurrencyValue in request_for_db['rates'].items():
         cur = conn.cursor()
         cur.execute("""UPDATE public."Currency" SET "CurrencyValue" = {} WHERE "ValueId" = '{}'""".format(CurrencyValue,ValueId))
         cur.execute("""UPDATE public."Currency" SET "LastUpdDate" = {} WHERE "ValueId" = '{}'""".format(request_for_db['timestamp'], ValueId))
         conn.commit()
    cur.close()
    conn.close()
    return


def main():
    schedule.every().day.at('00:00').do(data_update)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()




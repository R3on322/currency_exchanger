import psycopg2
from config.settings import DATABASES as db_conn
from .request import request
from .secrets import API_TOKEN,BASE_CURRENCY_URL
import time
import schedule


db_conn = db_conn['default']
class RequestToDB:

    connection = psycopg2.connect(
        host=db_conn['HOST'],
        user=db_conn['USER'],
        password=db_conn['PASSWORD'],
        database=db_conn['NAME'],
    )
    connection.close()
    def currencyfromdb(self):
        currency_values = {}
        try:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT "ValueId", "CurrencyValue" FROM "Currency"')
                for Currency, Value in cursor:
                    currency_values[Currency] = Value
                return currency_values

        except Exception as excp:
            print('Error while working with PostgreSQL', excp)

    #  need to update or rework
    def data_update(self):
        request_for_db = request(API_TOKEN, BASE_CURRENCY_URL)
        for ValueId, CurrencyValue in request_for_db['rates'].items():
            cursor = self.connection.cursor()
            cursor.execute("""UPDATE public."Currency" SET "CurrencyValue" = {} WHERE "ValueId" = '{}'""".format(CurrencyValue,ValueId))
            cursor.execute("""UPDATE public."Currency" SET "LastUpdDate" = {} WHERE "ValueId" = '{}'""".format(request_for_db['timestamp'], ValueId))
            self.connection.commit()
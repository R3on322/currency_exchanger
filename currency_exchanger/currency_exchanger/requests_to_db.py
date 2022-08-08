import psycopg2
from config.settings import DATABASES as db_conn
import schedule




db_conn = db_conn['default']
class RequestToDB:

    connection = psycopg2.connect(
        host=db_conn['HOST'],
        user=db_conn['USER'],
        password=db_conn['PASSWORD'],
        database=db_conn['NAME'],
    )

    def currencyfromdb(self):
        currency_values = {}
        try:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT "ValueId", "CurrencyValue" FROM "Currency" ')
                for Currency, Value in cursor:
                    currency_values[Currency] = Value
                return currency_values

        except Exception as excp:
            print('Error while working with PostgreSQL', excp)


    #  need to update or rework
    def data_update(self, request):
        for ValueId, CurrencyValue in request['rates'].items():
            cursor = connection.cursor()
            cursor.execute("""UPDATE public."Currency" SET "CurrencyValue" = {} WHERE "ValueId" = '{}'""".format(CurrencyValue, ValueId))
            cursor.execute("""UPDATE public."Currency" SET "LastUpdDate" = {} WHERE "ValueId" = '{}'""".format(request['timestamp'], ValueId))
            connection.commit()
        cursor.close()
        connection.close()
        return

def main():
    schedule.every().day.at('00:00').do(data_update)
    while True:
        schedule.run_pending()

if __name__ == '__main__':
    main()
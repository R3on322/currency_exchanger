import psycopg2
from config.settings import DATABASES as db_conn
from currency_exchanger.models import Currency
from currency_exchanger.request import request
from currency_exchanger.secrets import API_TOKEN, BASE_CURRENCY_URL


# db_conn = db_conn['default']
# class RequestToDB:
    # try:
    #     connection = psycopg2.connect(
    #         host=db_conn['HOST'],
    #         user=db_conn['USER'],
    #         password=db_conn['PASSWORD'],
    #         database=db_conn['NAME'],
    #     )
    # finally:
    #     connection.close()

    #  need to update or rework
    # def data_update_or_create(self, currency_data):
    #     data_from_db = Currency.object.all()
    #     print(data_from_db)


        # for ValueId, CurrencyValue in request_for_db['rates'].items():
        #     cursor = self.connection.cursor()
        #     cursor.execute("""UPDATE public."Currency" SET "CurrencyValue" = {} WHERE "ValueId" = '{}'""".format(CurrencyValue,ValueId))
        #     cursor.execute("""UPDATE public."Currency" SET "LastUpdDate" = {} WHERE "ValueId" = '{}'""".format(request_for_db['timestamp'], ValueId))
        #     self.connection.commit()

# currency_data = {'BTC': 4.1, 'EUR': 0.95, 'USD': 1, 'BRL': 5.9, 'ETH': 0.008}
# currency_data_old = {'BTC': 4.6026875e-05, 'EUR': 0.994555, 'USD': 1, 'BRL': 5.079705, 'ETH': 0.0005914}
# req_data = RequestToDB()
# req_data.data_update_or_create(currency_data)
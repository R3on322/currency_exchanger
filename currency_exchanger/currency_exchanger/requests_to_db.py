import psycopg2
# from config.settings import DATABASES as db_conn
from request import request
from secrets import API_TOKEN, BASE_CURRENCY_URL

# db_conn = db_conn['default']


# 'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'currencydb',
#         'USER': 'postgres',
#         'PASSWORD': 'newdb1337',
#         'HOST': '127.0.0.1',
#         'PORT': '5432'
class RequestToDB:
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password='newdb1337',
        database='currencydb',
    )

    def currency_from_db(self):
        currency_values = {}
        try:
            with self.connection.cursor() as cursor:
                cursor.execute('SELECT "ValueId", "CurrencyValue" FROM "Currency"')
                for Currency, Value in cursor:
                    currency_values[Currency] = Value
                return currency_values

        except Exception as excp:
            print('Error while working with PostgreSQL', excp)

    def create_table(self):
        # request_for_db = request(API_TOKEN, BASE_CURRENCY_URL)
        xdd ={'rates':{'BTC': 4.2305139e-05, 'EUR': 0.982045, 'USD': 1, 'BRL': 5.414199, 'ETH': 1579.43}}
        try:
            with self.connection.cursor() as cursor:
                for Value in xdd['rates']:
                    cursor.execute(
                        """INSERT INTO public."Currency" VALUES('{}',1,1)""".format(Value))
                    self.connection.commit()
        except Exception as excp:
            print('Error while working with PostgreSQL', excp)
        finally:
            self.connection.close()


    #  need to update or rework
    def data_update(self):
        request_for_db = request(API_TOKEN, BASE_CURRENCY_URL)
        for ValueId, CurrencyValue in request_for_db['rates'].items():
            cursor = self.connection.cursor()
            cursor.execute(
                """UPDATE public."Currency" SET "CurrencyValue" = {} WHERE "ValueId" = '{}'""".format(CurrencyValue,
                                                                                                      ValueId))
            cursor.execute("""UPDATE public."Currency" SET "LastUpdDate" = {} WHERE "ValueId" = '{}'""".format(
                request_for_db['timestamp'], ValueId))
            self.connection.commit()

RequestToDB().create_table()

"INSERT INTO fact_data (domain_desc,commodity_desc,statisticcat_desc,agg_level_desc,country_name,state_name,county_name,unit_desc,value,year) VALUES (" + ', '.join(map(str, (domain_desc,commodity_desc,statisticcat_desc,agg_level_desc,country_name,state_name,county_name,unit_desc,value1,year_val))) + ")"

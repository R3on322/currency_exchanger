import time

from currency_exchanger.models import Currency
from currency_exchanger.request import request
from currency_exchanger.secrets import API_TOKEN, BASE_CURRENCY_URL
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Create or update currency in database.'

    def handle(self, *args, **options):
        queryset = Currency.objects.all()
        currency_data_new = request(API_TOKEN, BASE_CURRENCY_URL)['rates']

        if options['update']:
            if len(queryset) == 0:
                print('The database is empty. Fill it out.')
            else:
                print('Updating exchange rate database...')
                for currency, value in currency_data_new.items():
                    Currency.objects.filter(ValueId=currency).update(CurrencyValue=value, LastUpdDate=time.time())
                self.stdout.write(self.style.SUCCESS('Courses successfully updated!'))

        else:
            print('Checking data from DB...')
            if not queryset:
                for currency, value in currency_data_new.items():
                    Currency.objects.create(ValueId=currency, CurrencyValue=value, LastUpdDate=time.time())
                self.stdout.write(self.style.SUCCESS('Database has been successfully filled in!'))
            else:
                print('DB not empty! Try to update("-u")')

    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--update',
            action='store_true',
            default=False,
            help='Update currency values'
        )

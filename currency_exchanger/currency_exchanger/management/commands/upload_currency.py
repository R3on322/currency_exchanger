import time

from currency_exchanger.models import Currency
from django.core.management.base import BaseCommand
from argparse import RawTextHelpFormatter


class Command(BaseCommand):
    help = 'Update or create currency in database.'

    def handle(self, *args, **options):
        if options['update']:
            print('Updating exchange rate database...')
            print('Courses successfully updated!')  # надо сделать обновление базы данных
        else:
            self.stdout.write(self.style.HTTP_INFO('Uploading data to DB...'))
            currency_data = {'BTC': 4.7857459e-05, 'EUR': 1.000455, 'USD': 1, 'BRL': 5.095899, 'ETH': 0.000621}
            currency_time = {'date': 20220827}
            queryset = Currency.objects.all()
            if not queryset:
                self.stdout.write(self.style.NOTICE('DB is Empty'))
                for currency, value in currency_data.items():
                    Currency.objects.create(ValueId=currency, CurrencyValue=value, LastUpdDate=time.time())
                self.stdout.write(self.style.SUCCESS('Database has been successfully filled in!'))
            else:
                self.stdout.write(self.style.WARNING('DB not empty, try to Update!'))

    def add_arguments(self, parser):
        # parser.add_argument(
        #     '-my', action='store_const', const=1234
        # )
        parser.add_argument(
            '-u',
            '--update',
            action='store_true',
            default=False,
            help='Update currency values'
        )

    def create_parser(self, prog_name, subcommand):
        parser = super(Command, self).create_parser(prog_name, subcommand)
        parser.formatter_class = RawTextHelpFormatter
        return parser

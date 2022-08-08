from django.contrib import admin
from .models import Currency

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('ValueId', 'CurrencyValue', 'LastUpdDate')

admin.site.register(Currency, CurrencyAdmin)

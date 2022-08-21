from django.urls import path
from .views import CurrencyView, ExchangerAPI


urlpatterns = [
    path('', CurrencyView.as_view({'get': 'list'}), name='currency_page'),
    path('api/exchanger/', ExchangerAPI.as_view(), name='currency_exchanger'),
]
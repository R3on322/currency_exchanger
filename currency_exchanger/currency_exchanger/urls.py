from django.urls import path
from .views import CurrencyView, ExchangerAPI


urlpatterns = [
    path('', CurrencyView.as_view()),
    path('api/exchanger/', ExchangerAPI.as_view()),
]
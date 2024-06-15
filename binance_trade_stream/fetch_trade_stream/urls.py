from django.urls import path
from .views import *

urlpatterns = [
    path('getTickerBySecond/<str:symbol>', getTickerBySecond, name='get_ticker_by_second'),
    path('getTickerByMin/<str:symbol>', getTickerByMin, name='get_ticker_by_min')
]
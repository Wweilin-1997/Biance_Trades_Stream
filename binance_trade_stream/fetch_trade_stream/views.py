from django.shortcuts import render
import pandas as pd
from rest_framework.response import Response


from rest_framework.decorators import api_view
from .models import BTCUSDT, SOLUSDT, XRPUSDT


# Create your views here.

tickers_mapping = {"btcusdt" : lambda : BTCUSDT.objects.order_by("-trade_time"),
                   "solusdt" : lambda : SOLUSDT.objects.order_by("-trade_time"),
                   "xrpusdt" : lambda : XRPUSDT.objects.order_by("-trade_time")}


@api_view(['GET'])
def getTickerBySecond(request, symbol) :
    df_data =  pd.DataFrame(reversed(list(tickers_mapping[symbol]()[:20000].values())))
    df_data["binance_latency"] = df_data['event_time'] - df_data['trade_time']
    df_data["transport_latency"] = df_data['received_time'] - df_data['event_time']

    df_data["trade_time"] = (df_data['trade_time'] // 1000) * 1000

    grouped_data = df_data.groupby('trade_time').agg({
        'binance_latency': "last",
        'transport_latency' : "last"
    }).reset_index()


    return Response({"message" : grouped_data.to_json(orient="records")})

@api_view(['GET'])
def getTickerByMin(request, symbol) :
    df_data =  pd.DataFrame(reversed(list(tickers_mapping[symbol]()[:50000].values())))
    df_data["binance_latency"] = df_data['event_time'] - df_data['trade_time']
    df_data["transport_latency"] = df_data['received_time'] - df_data['event_time']

    df_data["trade_time"] = (df_data['trade_time'] // 60000) * 60000

    grouped_data = df_data.groupby('trade_time').agg({
        'binance_latency': "last",
        'transport_latency' : "last"
    }).reset_index()


    return Response({"message" : grouped_data.to_json(orient="records")})



from django.urls import re_path

from binance_stream_consumer.consumers.BTCUSDTStream import BTCUSDTStream
from binance_stream_consumer.consumers.XRPUSDTStream import XRPUSDTStream
from binance_stream_consumer.consumers.SOLUSDTStream import SOLUSDTStream

websocket_urlpatterns = [
    re_path(r'ws/btcusdt@trade/$', BTCUSDTStream.as_asgi()),
    re_path(r'ws/solusdt@trade/$', SOLUSDTStream.as_asgi()),
    re_path(r'ws/xrpusdt@trade/$', XRPUSDTStream.as_asgi())
]
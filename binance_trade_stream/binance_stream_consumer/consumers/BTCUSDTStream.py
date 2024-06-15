import json
import time
from channels.generic.websocket import AsyncWebsocketConsumer
from confluent_kafka import Producer
import websockets


class BTCUSDTStream(AsyncWebsocketConsumer):
    async def connect(self):
        
        await self.accept()
        btcusdt_stream = "wss://stream.binance.com:9443/ws/btcusdt@trade"

        async with websockets.connect(btcusdt_stream) as websocket:
            while True:
                try:
                    response = await websocket.recv()
                    time_in_ms = time.time_ns() // 1000000;
                    data = json.loads(response)
                    event_time = data.get("E")
                    time_deltas = {"binance_latency" : event_time - data.get("T"),
                                   "transport_latency" : time_in_ms - event_time}

                    await self.send(text_data=json.dumps(time_deltas))
                except websockets.exceptions.ConnectionClosed:
                    pass

        

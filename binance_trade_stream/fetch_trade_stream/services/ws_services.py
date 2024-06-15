import websocket
import json
import time
from confluent_kafka import Producer

ws_api = "wss://stream.binance.com:9443/stream?streams=btcusdt@trade/xrpusdt@trade/solusdt@trade"

subscribe_tickers= ["btcusdt@trade", "xrpusdt@trade", "solusdt@trade"]
kafka_producer = Producer({'bootstrap.servers' : 'localhost:9092'})


def on_message(ws, message) :
    data = json.loads(message)
    kafka_producer.produce(data['stream'][:7] , message.encode('utf-8'))
    kafka_producer.flush()
    

def on_error(ws, error) :
    print(f"Error Encountered: Error {error}")
    print("Reconnecting...")

    time.sleep(3)
    connect_ws()

def on_close(ws, close_status_code, close_msg) :
    print(f"Connection closed. Status Code : {close_status_code}")
    time.sleep(3)

    connect_ws()

def connect_ws() :

    print("Connecting to WS")

    ws = websocket.WebSocketApp(ws_api, 
                                    on_message=on_message, 
                                    on_error=on_error, 
                                    on_close=on_close,
                                   )
    
    ws.run_forever()
    



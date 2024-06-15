import datetime
import json
from confluent_kafka import Consumer, KafkaError
import decimal

from ..models import *
from ..constants import *


def handle_btc_data_stream() :
    consumer = Consumer(btc_consumer_conf)
    consumer.subscribe(['btcusdt'])

    try:
        while True:
            print("hello")
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Reached end of partition: {msg.topic()} [{msg.partition()}]")
                else:
                    print(f"Error while consuming message: {msg.error()}")
            else:
                incoming = json.loads(msg.value().decode())["data"]
                print(incoming)
                new_datum = BTCUSDT(event_time=incoming["E"], trade_id=incoming["t"],
                                    price=decimal.Decimal(incoming["p"]), quantity=decimal.Decimal(incoming["q"]),
                                    buyer_trade_id=int(incoming["b"]), seller_trade_id=int(incoming["a"]), 
                                    trade_time=incoming["T"], buyer_mm=incoming["m"]== "True", 
                                    received_time=datetime.datetime.utcnow().timestamp())
                new_datum.save()

    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()

def handle_xrp_data_stream() :
    consumer = Consumer(xrp_consumer_conf)
    consumer.subscribe(['xrpusdt'])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Reached end of partition: {msg.topic()} [{msg.partition()}]")
                else:
                    print(f"Error while consuming message: {msg.error()}")
            else:
                incoming = json.loads(msg.value().decode())["data"]
                new_datum = XRPUSDT(event_time=incoming["E"], trade_id=incoming["t"],
                                    price=decimal.Decimal(incoming["p"]), quantity=decimal.Decimal(incoming["q"]),
                                    buyer_trade_id=int(incoming["b"]), seller_trade_id=int(incoming["a"]), 
                                    trade_time=incoming["T"], buyer_mm=incoming["m"]== "True",
                                    received_time=datetime.datetime.utcnow().timestamp())
                new_datum.save()

    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()


def handle_sol_data_stream() :
    consumer = Consumer(sol_consumer_conf)
    consumer.subscribe(['solusdt'])

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f"Reached end of partition: {msg.topic()} [{msg.partition()}]")
                else:  
                    print(f"Error while consuming message: {msg.error()}")
            else:
                incoming = json.loads(msg.value().decode())["data"]
                new_datum = SOLUSDT(event_time=incoming["E"], trade_id=incoming["t"],
                                    price=decimal.Decimal(incoming["p"]), quantity=decimal.Decimal(incoming["q"]),
                                    buyer_trade_id=int(incoming["b"]), seller_trade_id=int(incoming["a"]), 
                                    trade_time=incoming["T"], buyer_mm=incoming["m"]== "True",
                                    received_time=datetime.datetime.utcnow().timestamp())
                new_datum.save()



    except KeyboardInterrupt:
        print("Consumer stopped.")
    finally:
        consumer.close()
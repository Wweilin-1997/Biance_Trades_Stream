import json
import time
from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaError
import decimal


from ...models  import XRPUSDT


class Command(BaseCommand):
    help = 'Starts a XRPUSDT Kafka consumer'

    def handle(self, *args, **options):
        conf = {
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'xrpusdt',
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(conf)
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
                    print(incoming)    
                    new_datum = XRPUSDT(event_time=incoming["E"], trade_id=incoming["t"],
                                        price=decimal.Decimal(incoming["p"]), quantity=decimal.Decimal(incoming["q"]),
                                        buyer_trade_id=int(incoming["b"]), seller_trade_id=int(incoming["a"]), 
                                        trade_time=incoming["T"], buyer_mm=incoming["m"]== "True",
                                        received_time=time.time_ns() // 1000000)
                    new_datum.save()

        except KeyboardInterrupt:
            print("Consumer stopped.")
        finally:
            consumer.close()
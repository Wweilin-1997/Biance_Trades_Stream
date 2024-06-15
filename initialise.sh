#!/bin/bash'

NAME="Binance_Data_Streaming"
DJANGODIR=\\Users\\Home\\Documents\\Binance\\binance_trade_stream
ENVDIR=\\Users\\Home\\Documents\\Binance\\env\\Scripts\\activate

NUM_WORKERS=3
source $ENVDIR
cd $DJANGODIR

python manage.py makemigrations 
python manage.py migrate

python manage.py runserver &
P1=$!
python manage.py start_fetch_data &
P2=$!
python manage.py kafka_consumer_btcusdt &
P3=$!
python manage.py kafka_consumer_xrpusdt &
P4=$!
python manage.py kafka_consumer_solusdt &
P5=$!
daphne -p 8001 binance_trade_stream.asgi:application
P6=$!

wait $P1 $P2 $P3 $P4 $P5 $P6
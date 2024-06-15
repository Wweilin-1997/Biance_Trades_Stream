# Biance_Trades_Stream

This application is used to initialise a websocket with Binance Trade Steam API(https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md) and caluclate the latency on Binance Trade Data and Transport.

The data will be stored in a local dbsqlite3 database with the following fields are shown below:
{
  "event_time": 1672515782136,
  "symbol": "BNBBTC", 
  "trade_id": 12345,   
  "price": "0.001",    
  "quantity": "100",        
  "trade_time": 1672515782136, 
  "buyer_mm": true,          // Is the buyer the market maker?
}

The following pairs are used:
1. BTC/USDT
2. SOL/USDT
3. XRPUSDT

## Binance Latency 
This is being calculate using:
***event_time - trade_time<br><br>***

## Transport Latency 
This is being calculate using:
***TIME_ON_RECEVIING_DATA - event_time<br><br>***

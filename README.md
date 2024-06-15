# Biance_Trades_Stream

This is a Django application utilizing Django Channels to initialise and forward a websocket with Binance Trade Steam API(https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md) and calculate the latency on Binance Trade Data and Transport.

The data will be stored in a local dbsqlite3 database with the following fields are shown below: <br/><br/>
```javascript
{
  "event_time": 1672515782136,
  "symbol": "BNBBTC", 
  "trade_id": 12345,   
  "price": "0.001",    
  "quantity": "100",        
  "trade_time": 1672515782136, 
  "buyer_mm": true,          // Is the buyer the market maker?
}
```

The following pairs are used:
1. BTC/USDT
2. SOL/USDT
3. XRPUSDT

## Binance Latency 
This is calculated using:
***event_time - trade_time<br><br>***

## Transport Latency 
This is calculated using:
***TIME_ON_RECEVIING_DATA - event_time<br><br>***


## Application Architecture 
![image](https://github.com/Wweilin-1997/Biance_Trades_Stream/assets/72431929/4fe97089-a736-443e-a1ad-dad732c1ef2e)


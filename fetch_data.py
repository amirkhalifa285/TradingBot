import ccxt
import pandas as pd

def fetch_ohlcv(exchange_id='coinbase', symbol='BTC/USD', timeframe='1h', limit=100):
    exchange = getattr(ccxt, exchange_id)()
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    data = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit = 'ms')
    return data

if __name__ == "__main__":
    data = fetch_ohlcv()
    print(data.tail())
import ccxt

exchange = ccxt.coinbase()  # Initialize the Coinbase exchange
ticker = exchange.fetch_ticker('BTC/USD')
print(f"Last price of BTC/USD on Coinbase: {ticker['last']}")

ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='1m', limit=10)
print(ohlcv)

import pandas as pd

def identify_fvg(data):
    signals = []
    for i in range(2, len(data)):
        if data['high'][i] > data['high'][i-1] and data['high'][i-1] > data['high'][i-2]:
            fvg = {
                'type': 'up',
                'entry_zone': (data['low'][i-1], data['high'][i-1]),
                'stop_loss': data['low'][i-1],
                'take_profit': data['high'][i-1] + 2 * (data['high'][i-1] - data['low'][i-1]) # at least 2R 
            }
            signals.append(fvg)
        elif data['low'][i] < data['low'][i-1] and data['low'][i-1] < data['low'][i-2]:
            fvg = {
                'type': 'down',
                'entry_zone': (data['low'][i-1], data['high'][i-1]),
                'stop_loss': data['high'][i-1],
                'take_profit': data['low'][i-1] - 2 * (data['high'][i-1] - data['low'][i-1])
            }
            signals.append(fvg)
    return signals

if __name__ == "__main__":
    from backend.fetch_data import fetch_ohlcv
    data = fetch_ohlcv()

    signals = identify_fvg(data)
    print(signals)
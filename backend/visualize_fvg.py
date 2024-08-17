import json
import pandas as pd
from fetch_data import fetch_ohlcv
from strategy import identify_fvg

def get_fvg_data():
    # Fetch data with fewer candles (e.g., 10)
    data = fetch_ohlcv(limit=10)
    
    # Convert timestamp to string to make it JSON serializable
    data['timestamp'] = data['timestamp'].astype(str)
    
    signals = identify_fvg(data)
    return {
        'data': data.to_dict(orient='records'),  # Convert DataFrame to a list of records (dictionaries)
        'signals': signals
    }

if __name__ == "__main__":
    try:
        fvg_data = get_fvg_data()
        print(json.dumps(fvg_data))  # Output data as JSON
    except Exception as e:
        print(f"Error: {e}")

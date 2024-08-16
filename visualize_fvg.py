import mplfinance as mpf
import pandas as pd

def plot_candlestick_with_fvg(data, signals, max_signals=5):
    # Convert the DataFrame to a format suitable for mplfinance
    data = data.set_index('timestamp')

    # Prepare addplot list to hold FVG zones and other overlays
    addplots = []

    for signal in signals[:max_signals]:
        entry_zone_start = signal['entry_zone'][0]
        entry_zone_end = signal['entry_zone'][1]

        # Create a full-length series for the entry zone that spans all timestamps
        entry_zone_series_start = pd.Series([entry_zone_start] * len(data), index=data.index)
        entry_zone_series_end = pd.Series([entry_zone_end] * len(data), index=data.index)

        # Plot the FVG zone as an area plot between the entry zones
        addplots.append(mpf.make_addplot(entry_zone_series_start, color='green' if signal['type'] == 'up' else 'red', alpha=0.3))
        addplots.append(mpf.make_addplot(entry_zone_series_end, color='green' if signal['type'] == 'up' else 'red', alpha=0.3))

        # Add stop loss and take profit as horizontal lines for the entire length
        stop_loss_series = pd.Series(signal['stop_loss'], index=data.index)
        take_profit_series = pd.Series(signal['take_profit'], index=data.index)
        addplots.append(mpf.make_addplot(stop_loss_series, color='red', linestyle='--'))
        addplots.append(mpf.make_addplot(take_profit_series, color='green', linestyle='--'))

    # Plot the candlestick chart with custom addplots
    mpf.plot(data, type='candle', style='charles', addplot=addplots, title='Candlestick Chart with FVG Zones')

if __name__ == "__main__":
    from fetch_data import fetch_ohlcv
    from strategy import identify_fvg

    # Fetch data with fewer candles (e.g., 10)
    data = fetch_ohlcv(limit=10)
    signals = identify_fvg(data)

    # Plot the candlestick chart with FVG zones
    plot_candlestick_with_fvg(data, signals, max_signals=5)

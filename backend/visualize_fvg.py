import mplfinance as mpf
import pandas as pd

def plot_candlestick_with_fvg(data, signals, max_signals=1):  # Limit to 1 signal for simplicity
    # Convert the DataFrame to a format suitable for mplfinance
    data = data.set_index('timestamp')

    # Prepare addplot list to hold FVG zones and other overlays
    addplots = []

    for signal in signals[:max_signals]:
        entry_zone_start = signal['entry_zone'][0]
        entry_zone_end = signal['entry_zone'][1]

        # Create a shaded region for the FVG zone
        addplots.append(mpf.make_addplot(
            [entry_zone_start] * len(data), color='green' if signal['type'] == 'up' else 'red', alpha=0.2, panel=0))
        addplots.append(mpf.make_addplot(
            [entry_zone_end] * len(data), color='green' if signal['type'] == 'up' else 'red', alpha=0.2, panel=0))

        # Add stop loss and take profit as horizontal lines for the entire length
        stop_loss_series = pd.Series(signal['stop_loss'], index=data.index)
        take_profit_series = pd.Series(signal['take_profit'], index=data.index)
        addplots.append(mpf.make_addplot(stop_loss_series, color='red', linestyle='--', panel=0))
        addplots.append(mpf.make_addplot(take_profit_series, color='green', linestyle='--', panel=0))

    # Plot the candlestick chart with custom addplots
    mpf.plot(data, type='candle', style='charles', addplot=addplots, title='Candlestick Chart with FVG Zone')

if __name__ == "__main__":
    from backend.fetch_data import fetch_ohlcv
    from backend.strategy import identify_fvg

    # Fetch data with fewer candles (e.g., 10)
    data = fetch_ohlcv(limit=10)
    signals = identify_fvg(data)

    # Plot the candlestick chart with FVG zones
    plot_candlestick_with_fvg(data, signals, max_signals=1)  # Only show 1 FVG zone

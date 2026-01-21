import pandas as pd
from src.plots.plotting import plot_price, plot_with_indicators, plot_signals

df = pd.read_csv("data/raw/AAPL_2023-01-01_2023-12-31.csv", index_col=0, parse_dates=True)

# Simple plot
plot_price(df, "AAPL Price")

# Plot with SMA indicator example
from src.indicators.moving_averages import simple_moving_average
sma20 = simple_moving_average(df, window=20)

plot_with_indicators(df, {"SMA20": sma20}, "AAPL Price + SMA20")

# Example signals
buy = df["Close"] > sma20
sell = df["Close"] < sma20
plot_signals(df, buy, sell, "AAPL Buy/Sell Example")

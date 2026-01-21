import pandas as pd

def run_backtest(data, fast_window, slow_window):
    data = data.copy()

    # Flatten yfinance columns if needed
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data["Fast_SMA"] = data["Close"].rolling(fast_window).mean()
    data["Slow_SMA"] = data["Close"].rolling(slow_window).mean()

    data["Signal"] = 0
    data.loc[data["Fast_SMA"] > data["Slow_SMA"], "Signal"] = 1

    data["Strategy_Return"] = (
        data["Close"].pct_change() * data["Signal"].shift(1)
    )

    data["Cumulative_Strategy_Return"] = (
        1 + data["Strategy_Return"]
    ).cumprod()

    return data

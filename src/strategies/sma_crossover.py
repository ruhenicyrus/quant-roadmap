"""
sma_crossover.py

This module contains a clean strategy:
SMA 20 crosses SMA 50

It ONLY generates signals.
It DOES NOT execute trades.
"""

import pandas as pd
from src.indicators.moving_averages import simple_moving_average


def generate_signals(
    data: pd.DataFrame,
    short_window: int = 20,
    long_window: int = 50,
    price_column: str = "Close"
) -> pd.DataFrame:
    """
    Generate buy/sell signals based on SMA crossover.

    Buy signal: short SMA crosses above long SMA
    Sell signal: short SMA crosses below long SMA

    Parameters
    ----------
    data : pd.DataFrame
        Price data containing a price column
    short_window : int
        Short SMA window
    long_window : int
        Long SMA window
    price_column : str
        Column to calculate SMA on

    Returns
    -------
    pd.DataFrame
        Original data with added columns:
        - SMA_short
        - SMA_long
        - Signal
        - Position
    """

    if short_window >= long_window:
        raise ValueError("short_window must be smaller than long_window")

    # 1. Calculate indicators
    data["SMA_short"] = simple_moving_average(data, short_window, price_column)
    data["SMA_long"] = simple_moving_average(data, long_window, price_column)

    # 2. Generate raw signals
    data["Signal"] = 0
    data.loc[data["SMA_short"] > data["SMA_long"], "Signal"] = 1

    # 3. Prevent look-ahead bias:
    #    We use yesterday's signal as today's position
    data["Position"] = data["Signal"].shift(1).fillna(0)

    return data

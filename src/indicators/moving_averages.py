"""
moving_averages.py

This module contains pure indicator functions.
NO trading logic.
NO data downloading.
NO file saving.

Indicators take in data and return data.
"""

import pandas as pd


# =========================
# SIMPLE MOVING AVERAGE
# =========================

def simple_moving_average(
    data: pd.DataFrame,
    window: int,
    price_column: str = "Close"
) -> pd.Series:
    """
    Calculates a Simple Moving Average (SMA).

    Parameters
    ----------
    data : pd.DataFrame
        Price data containing a price column
    window : int
        Rolling window length
    price_column : str
        Column name to calculate SMA on

    Returns
    -------
    pd.Series
        SMA values
    """

    if price_column not in data.columns:
        raise KeyError(f"Column '{price_column}' not found in data")

    if window <= 0:
        raise ValueError("Window size must be positive")

    return data[price_column].rolling(window=window).mean()


# =========================
# EXPONENTIAL MOVING AVERAGE
# =========================

def exponential_moving_average(
    data: pd.DataFrame,
    window: int,
    price_column: str = "Close"
) -> pd.Series:
    """
    Calculates an Exponential Moving Average (EMA).

    Parameters
    ----------
    data : pd.DataFrame
        Price data containing a price column
    window : int
        Smoothing window
    price_column : str
        Column name to calculate EMA on

    Returns
    -------
    pd.Series
        EMA values
    """

    if price_column not in data.columns:
        raise KeyError(f"Column '{price_column}' not found in data")

    if window <= 0:
        raise ValueError("Window size must be positive")

    return data[price_column].ewm(span=window, adjust=False).mean()

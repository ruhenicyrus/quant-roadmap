import pandas as pd
import numpy as np


def calculate_daily_returns(data: pd.DataFrame) -> pd.Series:
    """
    Calculates daily returns for a price series.
    Input:
        data: DataFrame with a 'Close' column.
    Output:
        Series of daily returns.
    """
    return data["Close"].pct_change()


def calculate_strategy_returns(data: pd.DataFrame) -> pd.Series:
    """
    Calculates strategy returns using position column.
    Position must be shifted to avoid lookahead bias.
    Input:
        data: DataFrame with 'Position' and 'Daily_Return'
    Output:
        Series of strategy returns.
    """
    return data["Position"].shift(1) * data["Daily_Return"]


def calculate_cumulative_returns(returns: pd.Series) -> pd.Series:
    """
    Converts returns into cumulative returns.
    """
    return (1 + returns).cumprod()


def calculate_drawdown(cumulative_returns: pd.Series) -> pd.Series:
    """
    Calculates drawdown from cumulative returns.
    """
    peak = cumulative_returns.cummax()
    drawdown = (cumulative_returns - peak) / peak
    return drawdown


def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate=0.0) -> float:
    """
    Calculates annualized Sharpe Ratio.
    """
    excess_returns = returns - risk_free_rate / 252
    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()


def calculate_cagr(cumulative_returns: pd.Series) -> float:
    """
    Calculates Compound Annual Growth Rate (CAGR).
    Input:
        cumulative_returns: Series of cumulative returns
    Output:
        CAGR float
    """
    years = len(cumulative_returns) / 252
    total_return = cumulative_returns.iloc[-1]
    return total_return ** (1 / years) - 1

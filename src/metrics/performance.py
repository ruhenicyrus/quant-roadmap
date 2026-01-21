import numpy as np
import pandas as pd

def calculate_sharpe_ratio(returns: pd.Series, risk_free_rate=0.0):
    excess_returns = returns - risk_free_rate / 252
    return np.sqrt(252) * excess_returns.mean() / excess_returns.std()

def calculate_cagr(cumulative_returns: pd.Series):
    total_periods = cumulative_returns.shape[0]
    years = total_periods / 252
    return cumulative_returns.iloc[-1] ** (1 / years) - 1

def calculate_drawdown(cumulative_returns: pd.Series):
    peak = cumulative_returns.cummax()
    return (cumulative_returns - peak) / peak

# src/risk/metrics.py

import numpy as np
import pandas as pd


def max_drawdown(equity_curve: pd.Series) -> float:
    """
    Maximum Drawdown from equity curve.
    """
    peak = equity_curve.cummax()
    drawdown = (equity_curve - peak) / peak
    return drawdown.min()


def volatility(returns: pd.Series) -> float:
    """
    Annualized volatility.
    """
    return returns.std() * np.sqrt(252)


def calmar_ratio(cagr: float, max_dd: float) -> float:
    """
    Calmar Ratio = CAGR / |Max Drawdown|
    """
    if max_dd == 0:
        return np.nan
    return cagr / abs(max_dd)


def sortino_ratio(returns: pd.Series, risk_free_rate: float = 0.0) -> float:
    """
    Sortino ratio (downside risk)
    """
    downside_returns = returns[returns < 0]
    downside_std = downside_returns.std() * np.sqrt(252)
    excess_return = returns.mean() * 252 - risk_free_rate

    if downside_std == 0:
        return np.nan

    return excess_return / downside_std


def value_at_risk(returns: pd.Series, alpha: float = 0.05) -> float:
    """
    VaR at alpha level.
    """
    return np.percentile(returns.dropna(), alpha * 100)


def conditional_value_at_risk(returns: pd.Series, alpha: float = 0.05) -> float:
    """
    CVaR (Expected Shortfall)
    """
    var = value_at_risk(returns, alpha)
    return returns[returns <= var].mean()

# src/risk/risk_engine.py

import pandas as pd
from src.risk.metrics import (
    max_drawdown,
    volatility,
    calmar_ratio,
    sortino_ratio,
    value_at_risk,
    conditional_value_at_risk
)


def compute_risk_metrics(returns: pd.Series, equity_curve: pd.Series) -> dict:
    """
    Computes risk metrics for a strategy.
    """

    # Basic risk metrics
    dd = max_drawdown(equity_curve)
    vol = volatility(returns)

    # Performance risk ratios
    cagr = (equity_curve.iloc[-1]) ** (252 / len(equity_curve)) - 1
    calmar = calmar_ratio(cagr, dd)
    sortino = sortino_ratio(returns)

    # Tail risk
    var = value_at_risk(returns)
    cvar = conditional_value_at_risk(returns)

    return {
        "max_drawdown": dd,
        "volatility": vol,
        "cagr": cagr,
        "calmar_ratio": calmar,
        "sortino_ratio": sortino,
        "VaR": var,
        "CVaR": cvar
    }

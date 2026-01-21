# src/walkforward/out_of_sample_executor.py

import pandas as pd
from src.backtests.sma_backtest import run_backtest
from src.metrics.performance import calculate_cumulative_returns
from src.risk.risk_engine import compute_risk_metrics


def execute_out_of_sample(test_data: pd.DataFrame, fast_window: int, slow_window: int):
    """
    Executes strategy on OUT-OF-SAMPLE data using fixed parameters.
    """

    data = test_data.copy()

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    df = run_backtest(data, fast_window, slow_window)
    df = df.dropna()

    returns = df["Strategy_Return"]
    equity_curve = calculate_cumulative_returns(returns)

    risk_metrics = compute_risk_metrics(returns, equity_curve)

    return {
        "df": df,
        "returns": returns,
        "equity_curve": equity_curve,
        "risk_metrics": risk_metrics
    }

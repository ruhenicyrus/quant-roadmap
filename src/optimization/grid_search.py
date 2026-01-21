import pandas as pd
from src.backtests.sma_backtest import run_backtest
from src.metrics.performance import (
    calculate_sharpe_ratio,
    calculate_cagr,
    calculate_drawdown
)

def grid_search(fast_range, slow_range, data):
    results = []

    for fast in fast_range:
        for slow in slow_range:
            if fast >= slow:
                continue

            df = run_backtest(data, fast, slow)

            returns = df["Strategy_Return"].dropna()
            cumulative = df["Cumulative_Strategy_Return"].dropna()

            sharpe = calculate_sharpe_ratio(returns)
            cagr = calculate_cagr(cumulative)
            max_drawdown = calculate_drawdown(cumulative).min()

            results.append({
                "fast": fast,
                "slow": slow,
                "Sharpe": sharpe,
                "CAGR": cagr,
                "Max_Drawdown": max_drawdown
            })

    return pd.DataFrame(results)

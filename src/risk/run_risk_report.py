# src/risk/run_risk_report.py

import yfinance as yf
from src.backtests.sma_backtest import run_backtest
from src.metrics.performance import calculate_cumulative_returns
from src.risk.risk_engine import compute_risk_metrics

if __name__ == "__main__":
    data = yf.download("AAPL", start="2015-01-01")

    df = run_backtest(data, fast_window=20, slow_window=100)
    df = df.dropna()

    returns = df["Strategy_Return"]
    equity_curve = calculate_cumulative_returns(returns)

    risk_report = compute_risk_metrics(returns, equity_curve)
    print("RISK REPORT")
    print(risk_report)

# src/walkforward/run_optimizer_test.py

import yfinance as yf
from src.walkforward.in_sample_optimizer import optimize_sma_in_sample

if __name__ == "__main__":

    # Download long history
    data = yf.download("AAPL", start="2010-01-01")

    # Flatten MultiIndex (yfinance safety)
    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    # Use ONLY early portion as training
    train_data = data.loc["2010-01-01":"2015-01-01"]

    fast_range = [5, 10, 20]
    slow_range = [50, 100, 200]

    best_params = optimize_sma_in_sample(
        train_data,
        fast_range,
        slow_range
    )

    print("Best in-sample parameters:")
    print(best_params)

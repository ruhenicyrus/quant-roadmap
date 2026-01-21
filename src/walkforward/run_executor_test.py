# src/walkforward/run_executor_test.py

import yfinance as yf
from src.walkforward.out_of_sample_executor import execute_out_of_sample

if __name__ == "__main__":

    data = yf.download("AAPL", start="2015-01-01", end="2018-01-01")

    # Flatten columns
    if hasattr(data.columns, "levels"):
        data.columns = data.columns.get_level_values(0)

    # Pretend these came from in-sample optimization
    fast = 10
    slow = 50

    results = execute_out_of_sample(
        test_data=data,
        fast_window=fast,
        slow_window=slow
    )

    print("Out-of-sample Sharpe:", round(results["sharpe"], 3))
    print("Max Drawdown:", round(results["max_drawdown"], 3))

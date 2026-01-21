# src/walkforward/run_walkforward.py

import pandas as pd
from src.walkforward.splitter import rolling_train_test_split
from src.walkforward.in_sample_optimizer import optimize_in_sample
from src.walkforward.out_of_sample_executor import execute_out_of_sample


def run_walkforward(data, train_years=3, test_years=1, step_years=1):
    splits = rolling_train_test_split(
        data,
        train_years=train_years,
        test_years=test_years,
        step_years=step_years
    )

    stitched_results = []
    summary_results = []

    for i, split in enumerate(splits):
        print(f"\n=== Walk-Forward Split {i + 1} ===")

        train_data, test_data = split

        best_params = optimize_in_sample(
            train_data,
            fast_range=[5, 10, 15, 20],
            slow_range=[30, 50, 100, 200]
        )

        out_of_sample_result = execute_out_of_sample(
            test_data,
            best_params["fast"],
            best_params["slow"]
        )

        stitched_results.append(out_of_sample_result["df"])

        # Risk metrics
        rm = out_of_sample_result["risk_metrics"]

        summary_results.append({
            "split": i + 1,
            "fast": best_params["fast"],
            "slow": best_params["slow"],
            "sharpe": best_params["sharpe"],
            "max_drawdown": rm["max_drawdown"],
            "volatility": rm["volatility"],
            "sortino_ratio": rm["sortino_ratio"],
            "VaR": rm["VaR"],
            "CVaR": rm["CVaR"]
        })

    stitched_df = pd.concat(stitched_results)
    summary_df = pd.DataFrame(summary_results)

    return stitched_df, summary_df
if __name__ == "__main__":
    import yfinance as yf

    # Download data
    data = yf.download("AAPL", start="2010-01-01", end="2026-01-01")

    stitched, summary = run_walkforward(
        data,
        train_years=3,
        test_years=1,
        step_years=1
    )

    print("\n=== Walkforward Summary ===")
    print(summary)


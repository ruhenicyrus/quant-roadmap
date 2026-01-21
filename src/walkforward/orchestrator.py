# src/walkforward/orchestrator.py

import pandas as pd

from src.walkforward.splitter import generate_walkforward_splits
from src.optimization.grid_search import grid_search
from src.backtests.sma_backtest import run_backtest
from src.metrics.performance import (
    calculate_cumulative_returns,
    calculate_drawdown,
    calculate_sharpe_ratio
)


def run_walkforward(
    data: pd.DataFrame,
    fast_range,
    slow_range,
    train_years=3,
    test_years=1
):
    """
    Runs full walk-forward optimization and execution.

    Returns:
        stitched_out_of_sample_df
        summary_metrics
    """

    splits = generate_walkforward_splits(
        data,
        train_years=train_years,
        test_years=test_years
    )

    out_of_sample_results = []

    for i, split in enumerate(splits, start=1):
        print(f"\n=== Walk-Forward Split {i} ===")

        train_data, test_data = split

        # 🔹 1. Optimize on training data
        optimization_results = grid_search(
            fast_range,
            slow_range,
            train_data
        )

        best_params = optimization_results.sort_values(
            "Sharpe",
            ascending=False
        ).iloc[0]

        best_fast = int(best_params["fast"])
        best_slow = int(best_params["slow"])

        print(
            f"Best params | Fast={best_fast}, Slow={best_slow}"
        )

        # 🔹 2. Execute on out-of-sample data
        oos_df = run_backtest(
            test_data,
            best_fast,
            best_slow
        )

        oos_df["Split"] = i
        oos_df["Fast"] = best_fast
        oos_df["Slow"] = best_slow

        out_of_sample_results.append(oos_df)

    # 🔹 3. Stitch all OOS segments
    stitched = pd.concat(out_of_sample_results)

    stitched["Cumulative_Return"] = calculate_cumulative_returns(
        stitched["Strategy_Return"]
    )

    stitched["Drawdown"] = calculate_drawdown(
        stitched["Cumulative_Return"]
    )

    summary = {
        "Sharpe": calculate_sharpe_ratio(
            stitched["Strategy_Return"].dropna()
        ),
        "Max_Drawdown": stitched["Drawdown"].min(),
        "Total_Return": stitched["Cumulative_Return"].iloc[-1]
    }

    return stitched, summary

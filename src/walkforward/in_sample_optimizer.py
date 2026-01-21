# src/walkforward/in_sample_optimizer.py

import pandas as pd
from src.backtests.sma_backtest import run_backtest
from src.metrics.performance import calculate_sharpe_ratio


def optimize_in_sample(
    train_data: pd.DataFrame,
    fast_range: list,
    slow_range: list
):
    """
    Runs in-sample optimization on TRAINING data only.

    Parameters
    ----------
    train_data : pd.DataFrame
        Historical price data used ONLY for training.
    fast_range : list
        Candidate fast SMA windows.
    slow_range : list
        Candidate slow SMA windows.

    Returns
    -------
    dict
        Best parameters found in-sample.
    """

    best_sharpe = float("-inf")
    best_params = None

    # Loop through parameter grid
    for fast in fast_range:
        for slow in slow_range:

            # Rule: fast must be smaller than slow
            if fast >= slow:
                continue

            # --- RUN BACKTEST ON TRAIN DATA ONLY ---
            df = run_backtest(train_data, fast, slow)

            # Safety: drop NaNs created by rolling windows
            df = df.dropna()

            # If insufficient data, skip
            if len(df) < 50:
                continue

            # Calculate daily strategy returns
            returns = df["Strategy_Return"]

            # Calculate Sharpe (in-sample)
            sharpe = calculate_sharpe_ratio(returns)

            # Track best parameters
            if sharpe > best_sharpe:
                best_sharpe = sharpe
                best_params = {
                    "fast": fast,
                    "slow": slow,
                    "sharpe": sharpe
                }

    return best_params

import pandas as pd
from typing import List, Tuple


def rolling_train_test_split(
    data: pd.DataFrame,
    train_years: int = 3,
    test_years: int = 1,
    step_years: int = 1
) -> List[Tuple[pd.DataFrame, pd.DataFrame]]:
    """
    Generates rolling train/test splits for walk-forward optimization.
    """

    if not isinstance(data.index, pd.DatetimeIndex):
        raise ValueError("Data must have a DatetimeIndex")

    splits = []

    start_date = data.index.min()
    end_date = data.index.max()

    train_delta = pd.DateOffset(years=train_years)
    test_delta = pd.DateOffset(years=test_years)
    step_delta = pd.DateOffset(years=step_years)

    current_start = start_date

    while True:
        train_start = current_start
        train_end = train_start + train_delta

        test_start = train_end
        test_end = test_start + test_delta

        if test_end > end_date:
            break

        train_df = data.loc[train_start:train_end].copy()
        test_df = data.loc[test_start:test_end].copy()

        if len(train_df) == 0 or len(test_df) == 0:
            break

        splits.append((train_df, test_df))
        current_start += step_delta

    return splits

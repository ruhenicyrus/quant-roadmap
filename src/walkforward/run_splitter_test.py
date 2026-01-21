import yfinance as yf
from src.walkforward.splitter import rolling_train_test_split

data = yf.download("AAPL", start="2010-01-01")

splits = rolling_train_test_split(
    data,
    train_years=3,
    test_years=1,
    step_years=1
)

print(f"Number of splits: {len(splits)}")

for i, (train, test) in enumerate(splits):
    print(f"\nSplit {i + 1}")
    print(f"Train: {train.index.min().date()} → {train.index.max().date()}")
    print(f"Test : {test.index.min().date()} → {test.index.max().date()}")

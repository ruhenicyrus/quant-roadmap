import yfinance as yf
from src.optimization.grid_search import grid_search

if __name__ == "__main__":
    data = yf.download("AAPL", start="2015-01-01")

    fast_range = [5, 10, 20]
    slow_range = [50, 100, 200]

    results = grid_search(fast_range, slow_range, data)

    print(results.sort_values("Sharpe", ascending=False).head())

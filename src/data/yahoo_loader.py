
"""
yahoo_loader.py

This module is responsible for:
- Downloading market data from Yahoo Finance
- Performing basic validation
- Saving raw data safely to disk

This is the SINGLE source of truth for price data.
"""

import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import datetime


# =========================
# CONFIGURATION
# =========================

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


# =========================
# CORE FUNCTION
# =========================

def download_yahoo_data(
    symbol: str,
    start: str,
    end: str,
    overwrite: bool = False
) -> Path:
    """
    Downloads historical price data from Yahoo Finance.

    Parameters
    ----------
    symbol : str
        Ticker symbol (e.g. 'AAPL')
    start : str
        Start date in YYYY-MM-DD format
    end : str
        End date in YYYY-MM-DD format
    overwrite : bool
        Whether to overwrite existing raw data file

    Returns
    -------
    Path
        Path to saved CSV file
    """

    print(f"[INFO] Downloading data for {symbol} from {start} to {end}")

    data = yf.download(symbol, start=start, end=end)

    # -------------------------
    # VALIDATION CHECKS
    # -------------------------

    if data.empty:
        raise ValueError("Downloaded data is empty. Check symbol or dates.")

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    required_columns = {"Open", "High", "Low", "Close", "Volume"}
    missing = required_columns - set(data.columns)

    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    # -------------------------
    # FILE NAMING
    # -------------------------

    filename = f"{symbol}_{start}_{end}.csv"
    file_path = RAW_DATA_DIR / filename

    if file_path.exists() and not overwrite:
        raise FileExistsError(
            f"Raw data file already exists: {file_path}\n"
            f"Set overwrite=True if intentional."
        )

    data.to_csv(file_path)

    print(f"[SUCCESS] Data saved to {file_path}")
    print(f"[ROWS] {len(data)} rows")

    return file_path


# =========================
# SCRIPT ENTRY POINT
# =========================

if __name__ == "__main__":
    # Example manual test
    download_yahoo_data(
        symbol="AAPL",
        start="2023-01-01",
        end="2023-12-31",
        overwrite=False
    )

# ===========================
# week2_data_plot.py
# Quant Finance Roadmap – Week 2
# Fetch data, calculate returns, plot, and backtest MA crossover strategy
# ===========================

# Step 0: Imports
import yfinance as yf           # Download financial market data
import pandas as pd             # Data manipulation
import matplotlib.pyplot as plt # Plotting

# ===========================
# Step 1: Fetch historical price data for AAPL
# ===========================
data = yf.download("AAPL", start="2023-01-01", end="2023-12-31")

#Flatten the columns immediately after download-Flatten MultiIndex column
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)


# Display first 5 rows to verify
print("First 5 rows of downloaded data:")
print(data.head())

# ===========================
# Step 2: Calculate Daily Returns
# ===========================
# Daily Return = (Today Close - Yesterday Close) / Yesterday Close
data['Daily_Return'] = data['Close'].pct_change()

# Display first few rows to verify daily returns
print("\nDaily Returns:")
print(data[['Close', 'Daily_Return']].head())

# ===========================
# Step 3: Plot Daily Returns
# ===========================
plt.figure(figsize=(10,5))
plt.plot(data['Daily_Return'])
plt.title("Daily Returns of AAPL")
plt.xlabel("Date")
plt.ylabel("Return")
plt.show()


# ===========================
# Step 4: Moving Averages (SMA)
# ===========================
# 20-day and 50-day Simple Moving Averagesdata['SMA_20'] = data['Close'].rolling(window=20).mean()
data['SMA_50'] = data['Close'].rolling(window=50).mean()

# Plot price and moving averages
plt.figure(figsize=(12,6))
plt.plot(data['Close'], label='Close Price')
plt.plot(data['SMA_20'], label='SMA 20')
plt.plot(data['SMA_50'], label='SMA 50')
plt.title("AAPL Price with 20 & 50 Day SMA")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.show()

# ===========================
# Step 5: Generate Signals
# ===========================
# Signal = 1 if SMA_20 > SMA_50 (bullish), 0 otherwise
data['Signal'] = 0
data.loc[data['SMA_20'] > data['SMA_50'], 'Signal'] = 1

# Display last few rows
print("\nSignals based on SMA crossover:")
print(data[['Close', 'SMA_20', 'SMA_50', 'Signal']].tail())

# ===========================
# Step 6: Generate Positions
# ===========================
# Shift signals by 1 day to avoid look-ahead bias
data['Position'] = data['Signal'].shift(1)

# ===========================
# Step 7: Strategy Returns
# ===========================
# Strategy Return = Position * Daily Return
data['Strategy_Return'] = data['Position'] * data['Daily_Return']

# ===========================
# Step 8: Cumulative Returns (Equity Curve)
# ===========================
data['Cumulative_Market_Return'] = (1 + data['Daily_Return']).cumprod()
data['Cumulative_Strategy_Return'] = (1 + data['Strategy_Return']).cumprod()

# Plot Buy & Hold vs Strategy
plt.figure(figsize=(12,6))
plt.plot(data['Cumulative_Market_Return'], label='Buy & Hold')
plt.plot(data['Cumulative_Strategy_Return'], label='MA Crossover Strategy')
plt.title("Cumulative Returns: Strategy vs Market")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.legend()
plt.show()

# ===========================
# Step 9: Risk Measurement - Drawdown
# ===========================
# Compute rolling peak
data['Peak'] = data['Cumulative_Strategy_Return'].cummax()

# Compute drawdown = (Equity - Peak) / Peak
data['Drawdown'] = (data['Cumulative_Strategy_Return'] - data['Peak']) / data['Peak']

# Max drawdown
max_drawdown = data['Drawdown'].min()
print("\nMax Drawdown:", max_drawdown)

# ===========================
# Step 10: Key Performance Metrics
# ===========================
total_return = data['Cumulative_Strategy_Return'].iloc[-1] - 1
annualized_return = data['Strategy_Return'].mean() * 252        # Approx trading days
volatility = data['Strategy_Return'].std() * (252 ** 0.5)
sharpe_ratio = annualized_return / volatility

print("\nPerformance Metrics:")
print("Total Return:", total_return)
print("Annualized Return:", annualized_return)
print("Volatility:", volatility)
print("Sharpe Ratio:", sharpe_ratio)

# ===========================
# Step 11: Save data to Excel
# ===========================
data.to_excel("AAPL_2023_yfinance_data.xlsx", sheet_name="AAPL")
# ===========================
# Step 11: Save data to disk
# ===========================

# Save raw + processed data to CSV
data.to_csv("data/processed/AAPL_2023_strategy.csv")

# Save to Excel (requires openpyxl)
data.to_excel(
    "data/processed/AAPL_2023_strategy.xlsx",
    sheet_name="AAPL"
)

print("\n✅ Data exported successfully:")
print(" - CSV: data/processed/AAPL_2023_strategy.csv")
print(" - Excel: data/processed/AAPL_2023_strategy.xlsx")

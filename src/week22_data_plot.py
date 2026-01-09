# ===========================
# week2_data_plot.py
# Quant Finance Roadmap – Week 2
# ===========================

# ===========================
# 0️⃣ Imports
# ===========================
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ===========================
# 1️⃣ Fetch Historical Data
# ===========================
data = yf.download(
    "AAPL",
    start="2023-01-01",
    end="2023-12-31"
)

# ===========================
# 2️⃣ Normalize / Clean Data
# ===========================
# 🔥 FIX: Flatten MultiIndex columns immediately
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.get_level_values(0)

print("First 5 rows of downloaded data:")
print(data.head())

# ===========================
# 3️⃣ Feature Engineering
# ===========================

# ---- Daily Returns ----
data["Daily_Return"] = data["Close"].pct_change()

# ---- Moving Averages ----
data["SMA_20"] = data["Close"].rolling(window=20).mean()
data["SMA_50"] = data["Close"].rolling(window=50).mean()

# ===========================
# 4️⃣ Signal Generation
# ===========================
# 1 = long, 0 = flat
data["Signal"] = 0
data.loc[data["SMA_20"] > data["SMA_50"], "Signal"] = 1

# ===========================
# 5️⃣ Positioning (Avoid Look-Ahead Bias)
# ===========================
data["Position"] = data["Signal"].shift(1)

# ===========================
# 6️⃣ Strategy Returns
# ===========================
data["Strategy_Return"] = data["Position"] * data["Daily_Return"]

# ===========================
# 7️⃣ Cumulative Performance
# ===========================
data["Cumulative_Market_Return"] = (1 + data["Daily_Return"]).cumprod()
data["Cumulative_Strategy_Return"] = (1 + data["Strategy_Return"]).cumprod()

# ===========================
# 8️⃣ Risk Metrics (Drawdown)
# ===========================
data["Peak"] = data["Cumulative_Strategy_Return"].cummax()
data["Drawdown"] = (
    data["Cumulative_Strategy_Return"] - data["Peak"]
) / data["Peak"]

max_drawdown = data["Drawdown"].min()

# ===========================
# 9️⃣ Performance Metrics
# ===========================
total_return = data["Cumulative_Strategy_Return"].iloc[-1] - 1
annualized_return = data["Strategy_Return"].mean() * 252
volatility = data["Strategy_Return"].std() * (252 ** 0.5)
sharpe_ratio = annualized_return / volatility

print("\n📊 Performance Metrics")
print(f"Total Return: {total_return:.2%}")
print(f"Annualized Return: {annualized_return:.2%}")
print(f"Volatility: {volatility:.2%}")
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown:.2%}")

# ===========================
# 🔟 Visualization
# ===========================

# ---- Daily Returns ----
plt.figure(figsize=(10, 5))
plt.plot(data["Daily_Return"])
plt.title("Daily Returns of AAPL")
plt.xlabel("Date")
plt.ylabel("Return")
plt.show()

# ---- Price + Moving Averages ----
plt.figure(figsize=(12, 6))
plt.plot(data["Close"], label="Close")
plt.plot(data["SMA_20"], label="SMA 20")
plt.plot(data["SMA_50"], label="SMA 50")
plt.title("AAPL Price with Moving Averages")
plt.legend()
plt.show()

# ---- Equity Curve ----
plt.figure(figsize=(12, 6))
plt.plot(data["Cumulative_Market_Return"], label="Buy & Hold")
plt.plot(data["Cumulative_Strategy_Return"], label="MA Crossover Strategy")
plt.title("Cumulative Returns")
plt.ylabel("Growth of $1")
plt.legend()
plt.show()

# ===========================
# 1️⃣1️⃣ Save Outputs
# ===========================

# Ensure folders exist before saving
import os
os.makedirs("data/processed", exist_ok=True)

data.to_csv("data/processed/AAPL_2023_strategy.csv")
data.to_excel(
    "data/processed/AAPL_2023_strategy.xlsx",
    sheet_name="AAPL"
)

print("\n✅ Data exported successfully")

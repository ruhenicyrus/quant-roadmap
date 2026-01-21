import matplotlib.pyplot as plt
import pandas as pd


def plot_equity_curve(data: pd.DataFrame, title="Equity Curve"):
    """
    Plots cumulative returns.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data["Cumulative_Strategy_Return"], label="Strategy")
    plt.plot(data["Cumulative_Market_Return"], label="Buy & Hold")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_drawdown(data: pd.DataFrame, title="Drawdown"):
    """
    Plots drawdown curve.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data["Drawdown"], label="Drawdown")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()


import matplotlib.pyplot as plt

def plot_price(df, title="Price Chart"):
    """
    Plot the Close price from a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame containing 'Close'
        title (str): Title of the plot
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df["Close"], label="Close Price")
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_with_indicators(df, indicators, title="Price + Indicators"):
    """
    Plot Close price and indicator lines.

    Args:
        df (pd.DataFrame): DataFrame with Close
        indicators (dict): {"label": series}
        title (str): Title
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df["Close"], label="Close Price")

    for label, series in indicators.items():
        plt.plot(series, label=label)

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_signals(df, buy_signals, sell_signals, title="Buy/Sell Signals"):
    """
    Plot buy/sell markers on price chart.

    Args:
        df (pd.DataFrame): DataFrame with Close
        buy_signals (pd.Series): True/False
        sell_signals (pd.Series): True/False
        title (str): Title
    """
    plt.figure(figsize=(12, 6))
    plt.plot(df["Close"], label="Close Price")

    plt.scatter(df.index[buy_signals], df["Close"][buy_signals], marker="^", label="Buy", s=100)
    plt.scatter(df.index[sell_signals], df["Close"][sell_signals], marker="v", label="Sell", s=100)

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.show()

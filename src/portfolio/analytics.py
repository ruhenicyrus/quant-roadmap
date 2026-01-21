import numpy as np

def portfolio_volatility(returns):
    return np.std(returns) * np.sqrt(252)

def portfolio_cagr(returns):
    cumulative = (1 + returns).cumprod()
    years = len(returns) / 252
    return cumulative.iloc[-1] ** (1 / years) - 1

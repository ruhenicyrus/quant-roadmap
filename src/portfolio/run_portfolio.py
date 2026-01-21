from src.portfolio.weights import equal_weight
from src.portfolio.portfolio import Portfolio

def run_portfolio(asset_returns):
    weights = equal_weight(asset_returns.keys())
    portfolio = Portfolio(asset_returns, weights)
    return portfolio.compute_portfolio_returns()

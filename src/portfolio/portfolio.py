import pandas as pd

class Portfolio:
    def __init__(self, asset_returns, weights):
        self.asset_returns = asset_returns
        self.weights = weights

    def compute_portfolio_returns(self):
        df = pd.DataFrame(self.asset_returns)
        for asset in df.columns:
            df[asset] *= self.weights[asset]
        return df.sum(axis=1)

class AssetUniverse:
    def __init__(self, assets):
        """
        assets: dict
        {
            "SPY": dataframe,
            "BTC": dataframe,
            "GLD": dataframe
        }
        """
        self.assets = assets

    def list_assets(self):
        return list(self.assets.keys())

    def get_data(self, asset):
        return self.assets[asset]

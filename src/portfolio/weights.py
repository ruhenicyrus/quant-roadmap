import numpy as np

def equal_weight(assets):
    n = len(assets)
    return {asset: 1 / n for asset in assets}


def risk_parity(vols):
    inv_vol = {k: 1 / v for k, v in vols.items()}
    total = sum(inv_vol.values())
    return {k: v / total for k, v in inv_vol.items()}

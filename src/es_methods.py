import numpy as np
import pandas as pd

def historical_es(returns, weights, alpha=0.05, horizon=1, portfolio_value=1.0):
    weighted_returns = returns.dot(weights)
    horizon_returns = weighted_returns.rolling(horizon).sum().dropna()
    cutoff = np.percentile(horizon_returns.values, alpha * 100)
    es = -horizon_returns[horizon_returns <= cutoff].mean() * portfolio_value
    return es

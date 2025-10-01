# tools for portfoilio simulation, specifically using MC (multiple paths / simulations)

import numpy as np

def simulate_portfolio_paths(returns, weights, horizon=10, sims=10000, seed=None):
    if seed:
        np.random.seed(seed)
    mu = returns.mean().values
    cov = returns.cov().values
    paths = np.random.multivariate_normal(mu, cov, size=(sims, horizon))
    portfolio_paths = paths @ weights
    return portfolio_paths

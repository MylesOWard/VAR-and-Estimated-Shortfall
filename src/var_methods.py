# src/var_methods.py

import numpy as np
import pandas as pd
from scipy.stats import norm
from typing import Union


def historical_var(
    returns: Union[pd.Series, pd.DataFrame],
    weights: np.ndarray = None,
    alpha: float = 0.05,
    horizon: int = 1,
    portfolio_value: float = 1.0
) -> float:
    """
    Historical Value-at-Risk (VaR) using rolling returns.

    Parameters
    ----------
    returns : Series or DataFrame
        Daily log returns. If DataFrame, must provide weights.
    weights : array-like, optional
        Portfolio weights. Required if returns is a DataFrame.
    alpha : float, default=0.05
        Significance level (e.g. 0.05 for 95% VaR).
    horizon : int, default=1
        Time horizon in days.
    portfolio_value : float, default=1.0
        Current portfolio value.

    Returns
    -------
    float
        Historical VaR estimate (positive number, in portfolio currency).
    """
    if isinstance(returns, pd.DataFrame):
        if weights is None:
            raise ValueError("Weights must be provided when returns is a DataFrame.")
        weighted_returns = returns.dot(weights)
    else:
        weighted_returns = returns

    horizon_returns = weighted_returns.rolling(horizon).sum().dropna()
    var_value = -np.percentile(horizon_returns.values, alpha * 100) * portfolio_value
    return var_value


def parametric_var(
    returns: Union[pd.Series, pd.DataFrame],
    weights: np.ndarray = None,
    alpha: float = 0.05,
    horizon: int = 1,
    portfolio_value: float = 1.0
) -> float:
    """
    Parametric (Gaussian) Value-at-Risk (VaR).

    Parameters
    ----------
    returns : Series or DataFrame
        Daily log returns. If DataFrame, must provide weights.
    weights : array-like, optional
        Portfolio weights. Required if returns is a DataFrame.
    alpha : float, default=0.05
        Significance level (e.g. 0.05 for 95% VaR).
    horizon : int, default=1
        Time horizon in days.
    portfolio_value : float, default=1.0
        Current portfolio value.

    Returns
    -------
    float
        Parametric VaR estimate (positive number, in portfolio currency).
    """
    if isinstance(returns, pd.DataFrame):
        if weights is None:
            raise ValueError("Weights must be provided when returns is a DataFrame.")
        weighted_returns = returns.dot(weights)
    else:
        weighted_returns = returns

    mu = weighted_returns.mean()
    sigma = weighted_returns.std()

    horizon_mu = horizon * mu
    horizon_sigma = np.sqrt(horizon) * sigma

    var_value = -(horizon_mu + horizon_sigma * norm.ppf(alpha)) * portfolio_value
    return var_value


def monte_carlo_var(
    returns: pd.DataFrame,
    weights: np.ndarray,
    alpha: float = 0.05,
    horizon: int = 5,
    sims: int = 10000,
    portfolio_value: float = 1.0,
    seed: int = None
) -> float:
    """
    Monte Carlo Value-at-Risk (VaR) using multivariate normal simulation.

    Parameters
    ----------
    returns : DataFrame
        Daily log returns of portfolio assets.
    weights : array-like
        Portfolio weights.
    alpha : float, default=0.05
        Significance level (e.g. 0.05 for 95% VaR).
    horizon : int, default=5
        Time horizon in days.
    sims : int, default=10000
        Number of Monte Carlo simulations.
    portfolio_value : float, default=1.0
        Current portfolio value.
    seed : int, optional
        Random seed for reproducibility.

    Returns
    -------
    float
        Monte Carlo VaR estimate (positive number, given in portfolio currency).
    """
    if seed is not None:
        np.random.seed(seed)

    mu = returns.mean().values
    cov = returns.cov().values

    simulated_paths = np.random.multivariate_normal(mu, cov, size=(sims, horizon))
    simulated_weighted = simulated_paths @ weights
    simulated_total = simulated_weighted.sum(axis=1)

    var_value = -np.percentile(simulated_total, alpha * 100) * portfolio_value
    return var_value

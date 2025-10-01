import yfinance as yf
import numpy as np
from src.var_methods import historical_var, parametric_var, monte_carlo_var

tickers = ["SPY", "BND", "GLD", "QQQ", "VTI"]
data = yf.download(tickers, start="2020-01-01", end="2025-01-01")["Close"]
log_returns = np.log(data / data.shift(1)).dropna()

weights = np.array([0.2] * len(tickers))
pv = 1_000_000

print("Historical VaR:", historical_var(log_returns, weights, portfolio_value=pv))
print("Parametric VaR:", parametric_var(log_returns, weights, portfolio_value=pv))
print("Monte Carlo VaR:", monte_carlo_var(log_returns, weights, portfolio_value=pv))

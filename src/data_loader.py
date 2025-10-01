import yfinance as yf
import pandas as pd
import numpy as np

def load_returns(tickers, start="2020-01-01", end="2025-01-01"):
    data = yf.download(tickers, start=start, end=end)["Close"]
    log_returns = np.log(data / data.shift(1)).dropna()
    return log_returns

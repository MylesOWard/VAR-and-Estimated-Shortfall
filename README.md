# VAR-and-Estimated-Shortfall

### Quantitative Risk Modelling with Python

This repository implements and compares multiple Value-at-Risk (VaR) estimation techniques — from historical methods to full Monte Carlo simulation — along with Expected Shortfall (CVaR) and backtesting.

It’s structured as a modular research toolkit, with reusable code in `src/` and six polished Jupyter notebooks demonstrating theory, implementation, and validation. Data for this project was sourced from Yahoo Finance, it has been stored locally to avoid pull request limits.

---

## Project Overview

Value-at-Risk (VaR) measures the maximum expected loss over a given time horizon at a specified confidence level (e.g. 95%).  
This repo explores three major approaches:

| Method | Description | Pros | Cons |
|:--|:--|:--|:--|
| **Historical VaR** | Quantile of historical returns | Simple & non-parametric | Ignores correlations |
| **Parametric / Gaussian VaR** | Assumes returns are normally distributed | Fast & analytical | Unrealistic for fat tails |
| **Monte Carlo VaR** | Simulates returns under a statistical model | Flexible & general | Computationally expensive |

In addition, this code covers include Expected Shortfall (CVaR), a risk measure that captures the average loss beyond VaR, and Kupiec backtesting to validate model accuracy.

---

## Notebook Series

All notebooks include inline figures, explanations, and example outputs.

| # | Notebook | Focus |
|:--|:--|:--|
| 01 | [`01_simple_var.ipynb`](notebooks/01_simple_var.ipynb) | Basic Historical VaR on single asset |
| 02 | [`02_es_methods.ipynb`](notebooks/02_es_methods.ipynb) | Expected Shortfall (CVaR) |
| 03 | [`03_mc_var.ipynb`](notebooks/03_mc_var.ipynb) | Monte Carlo VaR with multi-asset portfolio |
| 04 | [`04_var_comparison.ipynb`](notebooks/04_var_comparison.ipynb) | Compare Historical, Parametric, Monte Carlo VaR |
| 05 | [`05_backtesting_var.ipynb`](notebooks/05_backtesting_var.ipynb) | VaR backtesting with Kupiec test |
| 06 | [`06_portfolio_projections.ipynb`](notebooks/06_portfolio_projections.ipynb) | Monte Carlo portfolio projections (multi-horizon) |

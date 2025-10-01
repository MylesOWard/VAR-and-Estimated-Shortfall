# just helper functions

import matplotlib.pyplot as plt

def plot_var_distribution(returns, var_value, alpha=0.05):
    plt.hist(returns, bins=50, alpha=0.7)
    plt.axvline(-var_value, color="red", linestyle="--", label=f"VaR {int((1-alpha)*100)}%")
    plt.legend()
    plt.show()

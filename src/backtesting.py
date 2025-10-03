import numpy as np
from scipy.stats import chi2

def kupiec_test(breaches, total_obs, alpha = 0.05):
    expected = alpha * total_obs
    p_hat = breaches / total_obs
    LR = -2 * ( 
        np.log(((1 - alpha) ** (total_obs - breaches) * (alpha ** breaches))) -
        np.log(((1 - p_hat) ** (total_obs - breaches) * (p_hat ** breaches)))
    )
    p_value = 1 - chi2.cdf(LR, 1)
    return LR, p_value

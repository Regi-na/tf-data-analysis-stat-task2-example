import pandas as pd
import numpy as np

from scipy.stats import norm, chi2, kurtosis



chat_id = 947352272 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    s2 = np.var(x)
    l = n - 1  
    #return s2 * np.sqrt(l / chi2.ppf(1 - alpha / 2, l)), \
          # s2 * np.sqrt(l / chi2.ppf(alpha / 2, l))
    #return np.sqrt(s2**2 * n / chi2.ppf(1 - alpha / 2, n)), \
     #      np.sqrt(s2**2 * n / chi2.ppf(alpha / 2, n))
    return np.std(x)/(32**0.5) * l /chi2.ppf(alpha / 2, df = l) * np.mean(x), \
           np.std(x)/(32**0.5) * l / chi2.ppf(1-alpha / 2, df = l) * np.mean(x)

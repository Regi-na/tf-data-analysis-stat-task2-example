import pandas as pd
import numpy as np

from scipy.stats import norm, chi2



chat_id = 947352272 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    s2 = np.var(x, ddof=1)
    l = n - 1  
    return x.std() - np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)), \
           x.std() - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x))

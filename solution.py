import pandas as pd
import numpy as np

from scipy.stats import norm, chi2



chat_id = 947352272 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = len(x)
    scale = np.var(x, ddof = 1)**2
    return loc * scale / chi2.ppf(1 - alpha / 2, df = len(x)), \
           loc * scale / chi2.ppf(alpha / 2, df = len(x))

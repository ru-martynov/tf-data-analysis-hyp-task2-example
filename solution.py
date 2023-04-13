import pandas as pd
import numpy as np

chat_id = 303100650 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    from scipy.stats import anderson_ksamp


    alpha = 0.01
    Anderson_Darling_test = anderson_ksamp([x, y])
    stat, p_value = Anderson_Darling_test.statistic, Anderson_Darling_test.pvalue
    answer = p_value < alpha
    return answer

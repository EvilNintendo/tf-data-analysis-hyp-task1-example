import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 134277149 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)
    # Вычисляем z-статистику
    z = (p1 - p2) / np.sqrt(p * (1 - p) * (1/x_cnt + 1/y_cnt))
    # Вычисляем критическое значение z
    z_critical = norm.ppf(1 - 0.06/2)
    # Проверяем, попадает ли z в доверительный интервал
    if abs(z) > z_critical:
        return True
    else:
       return False

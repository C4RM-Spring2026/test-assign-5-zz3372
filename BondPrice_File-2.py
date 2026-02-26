import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    t = np.arange(1, n + 1, dtype=float)
    df = (1.0 + r) ** (-t)
    c = face * couponRate / ppy
    return c * df.sum() + face * df[-1]

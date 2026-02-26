import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy

    k = np.arange(1, n + 1, dtype=float)
    t = k / ppy
    df = (1.0 + r) ** (-k)

    c = face * couponRate / ppy
    cf = np.full(n, c, dtype=float)
    cf[-1] += face

    pvcf = cf * df
    price = pvcf.sum()

    return (t * pvcf).sum() / price

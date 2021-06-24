import numpy as np
def batchnorm_forward(x, gamma, beta, eps):
    N, D = x.shape
    # 1.均值
    mu = 1./N * np.sum(x, axis=0)
    # 2.减去均值
    xmu = x - mu
    # 3.方差
    sq = xmu ** 2
    var = 1./N * np.sum(sq, axis=0)
    # 4.规范化的分母
    sqrtvar = np.sqrt(var + eps)
    ivar = 1./sqrtvar
    # 5. normalization
    xhat = xmu * ivar
    # 6. scale and shift
    gammax = gamma * xhat
    out = gammax + beta
    # 存储中间变量
    cache = (xhat, gamma, xmu, ivar, sqrtvar, var, eps)
    return out, cache
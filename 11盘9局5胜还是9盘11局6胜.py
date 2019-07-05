from matplotlib import pyplot as plt
import numpy as np
from scipy.special import comb


def f(p, n):
    assert n % 2 != 0
    m = (n + 1) // 2
    result = 0
    for i in range(m, n + 1):
        result += comb(n, i) * np.power(p, i) * np.power((1 - p), n - i)
    return result
    

def r(p):
    return p * (1 - p)


def df(p, n):
    assert n % 2 != 0
    m = (n - 1) // 2
    return n * comb(2 * m, m) * np.power(r(p), m) 


def draw(func, *args):
    t_list = []
    p_range = list(np.linspace(0.5, 1, 20))
    for p in p_range:
        t_list.append(func(p, *args))
    plt.plot(p_range, t_list, label=str(args))


def ff(p, a, b):
    return f(f(p, b), a)


def dff(p, a, b):
    q_b = f(p, b)
    return df(q_b, a) * df(p, b)


def srl(p, a):
    q_a = f(p, a)
    return np.power(r(q_a) / r(p), 2 / (a - 1))


def dsrl(p, a):
    d_s = srl(p, a)
    d_s_plus = srl(p, a + 2)
    d_s_minus = srl(p, a - 2)
    return d_s_plus * d_s_minus / d_s / d_s


# draw(ff, 11, 9)
# draw(ff, 9, 11)


# draw(dff, 33, 3)
# draw(dff, 3, 33)


# for i in range(3, 33, 2):
#     draw(srl, i)


for i in range(5, 25, 2):
    draw(dsrl, i)


plt.xlabel('t')
plt.ylabel('p')
plt.legend()
plt.show()


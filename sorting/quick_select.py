import numpy as np


def quick_select(S, k):
    n = len(S)
    if n == 1:
        return S[0]
    pivot = np.random.choice(S)
    L = [e for e in S if e < pivot]
    E = [e for e in S if e == pivot]
    G = [e for e in S if e > pivot]

    if k <= len(L):
        return quick_select(L, k)
    elif k <= len(L) + len(E):
        return pivot
    else:
        j = k - len(L) - len(E)
        return quick_select(G, j)

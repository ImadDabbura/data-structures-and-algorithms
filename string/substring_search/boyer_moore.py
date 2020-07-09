"""Implementation of Boyer-Moore algorithm of substring search."""


def find_boyer_moore(T, P):
    """Return the index of first occurance of P; otherwise, returns -1."""
    n, m = len(T), len(P)
    if m == 0:
        return 0
    last = {k: i for i, k in enumerate(P)}
    i = k = m - 1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            i -= 1
            k -= 1
        else:
            j = last.get(T[i], -1)
            i += m - min(k, j + 1)
            k = m - 1
    return -1

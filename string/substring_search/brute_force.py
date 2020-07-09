"""Implementation of Brute-Force algorithm of substring search."""


def find_brute_force(T, P):
    """Return the index of first occurance of P; otherwise, returns -1."""
    n, m = len(T), len(P)
    if m == 0:
        return 0
    for i in range(n - m + 1):
        j = 0
        while j < m and T[i + j] == P[j]:
            j += 1
        if j == m:
            return i
    return -1


def find_brute_force_v1(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0
    i = j = 0
    while i < n and j < m:
        if T[i] == P[j]:
            j += 1
        else:
            i -= j
            j = 0
        i += 1
    if j == m:
        return i - m
    return -1

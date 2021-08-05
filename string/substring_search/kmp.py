"""Implementation of Knuth-Morris-Pratt algorithm of substring search."""


def compute_lps_table(P):
    """Computes the longest prefix suffix table for KMP algorithm."""
    m = len(P)
    lps_table = [0] * m
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            lps_table[j] = k + 1
            j += 1
            k += 1
        # k follows matching prefix
        elif k > 0:
            k = lps_table[k - 1]
        # no match found at index j
        else:
            j += 1
    return lps_table


def find_kmp(T, P):
    """Return the index of first occurance of P; otherwise, returns -1."""
    n, m = len(T), len(P)
    if m == 0:
        return 0
    lps_table = lps(P)
    j = k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = lps_table[k - 1]
        else:
            j += 1
    return -1

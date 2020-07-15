"""Implementation of Rabin-Karp algorithm of substring search."""


def find_rabin_karp(T, P):
    """Return the index of first occurance of P; otherwise, returns -1."""
    n = len(T)
    m = len(P)
    t_hash = 0
    p_hash = 0
    h = 1
    d = 256  # Alphabet size
    q = 109_345_121  # Any large number >= m would work,
    # larger q --> lower probability for collisions

    for _ in range(m - 1):
        h = (h * d) % q

    # Calculate the hash value of the text and the pattern
    # for the first window:
    # p_hash = ord(P[0]) * d ** (m - 1) + ord(P[1]) * d ** (m - 2)
    for i in range(m):
        p_hash = (d * p_hash + ord(P[i])) % q
        t_hash = (d * t_hash + ord(T[i])) % q

    for i in range(n - m + 1):
        if p_hash == t_hash:
            # check if all characters are equal
            # (since hash values may be equal due to collisions)
            for k in range(m):
                if T[i + k] != P[k]:
                    break
            if k == m - 1:
                return i
        if i < n - m:
            # Rehashing: remove leading digit, add trailing digit
            t_hash = (d * (t_hash - ord(T[i]) * h) + ord(T[i + m])) % q
    return -1

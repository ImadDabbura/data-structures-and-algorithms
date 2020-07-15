"""Implementation of least significant digit (LSD) Radix Sorting."""


def lsd(L, w):
    n = len(L)
    R = 256

    for d in range(w - 1, -1, -1):
        count = [0] * (R + 1)

        # Build freq counts
        for key in L:
            count[ord(key[d]) + 1] += 1

        # Comp cumsum
        for i in range(R):
            count[i + 1] += count[i]

        # Distribute keys
        tmp = [0] * n
        for key in L:
            tmp[count[ord(key[d])]] = key
            count[ord(key[d])] += 1

        # Copy back sorted key to list
        for i, key in enumerate(tmp):
            L[i] = key

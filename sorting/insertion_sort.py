def insertion_sort(L):
    """Implementation of insertion sort."""
    n = len(L)
    if n < 2:
        return L
    for i in range(1, n):
        tmp = L[i]
        j = i
        while j > 0 and tmp < L[j - 1]:
            L[j] = L[j - 1]
            j -= 1
        L[j] = tmp

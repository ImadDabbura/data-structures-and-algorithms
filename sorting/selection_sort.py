def selection_sort(L):
    """Implementation of selection sort."""
    n = len(L)
    if n < 2:
        return L
    for i in range(n - 1):
        smallest_idx = i
        for j in range(i + 1, n):
            if L[j] < L[smallest_idx]:
                smallest_idx = j
        if smallest_idx != i:
            L[smallest_idx], L[i] = L[i], L[smallest_idx]

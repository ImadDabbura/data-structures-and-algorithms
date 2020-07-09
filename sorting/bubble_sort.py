def bubble_sort(L):
    """Implementation of bubble sort."""
    n = len(L)
    if n < 2:
        return L
    for i in range(n - 1):
        is_sorted = True
        for j in range(n - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
                is_sorted = False
        if is_sorted:
            break

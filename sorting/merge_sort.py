def merge(L, left, right):
    """Merge two sorted lists."""
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            L[i + j] = left[i]
            i += 1
        else:
            L[i + j] = right[j]
            j += 1
    while i < len(left):
        L[i + j] = left[i]
        i += 1
    while j < len(right):
        L[i + j] = right[j]
        j += 1


def merge_sort(L):
    """Implementation of merge sort."""
    n = len(L)
    if n < 2:
        return L
    mid = n // 2
    left = L[:mid]
    right = L[mid:]
    merge_sort(left)
    merge_sort(right)
    merge(L, left, right)

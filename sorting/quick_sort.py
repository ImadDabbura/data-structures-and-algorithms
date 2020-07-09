import numpy as np


def quick_sort(L):
    """Implementation of randomized quick sort."""
    n = len(L)
    if n < 2:
        return L
    pivot = np.random.choice(L)
    left = [e for e in L if e <= pivot]
    right = [e for e in L if e > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

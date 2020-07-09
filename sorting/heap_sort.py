class HeapSort:
    """Sort implementation using min-heap."""

    @staticmethod
    def sort(arr):
        n = len(arr)
        HeapSort._heapify(arr)
        for i in range(1, n):
            HeapSort._swap(arr, 0, n - i)
            HeapSort._downheap(arr, 0, n - i)

    @staticmethod
    def _swap(arr, i, j):
        """In-place swapping."""
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def _heapify(arr):
        """Construct heap from array."""
        n = len(arr)
        parent = (n - 1) // 2
        for i in range(parent, -1, -1):
            HeapSort._downheap(arr, i, n)

    @staticmethod
    def _downheap(arr, i, j):
        """Down-heap starting at i and end at j."""
        if (2 * i) + 1 < j:
            child = left = (2 * i) + 1
            if (2 * j) + 2 < j:
                right = (2 * j) + 2
                if arr[right] < arr[left]:
                    child = right
            if arr[child] < arr[i]:
                HeapSort._swap(arr, child, i)
                HeapSort._downheap(arr, child, j)

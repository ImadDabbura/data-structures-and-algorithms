"""
HeapPriorityQueue: Implementation of Priority Queue ADT adaptable heap data structure as well as HeapSort. It is an array-based implementation.
"""
from .simple_priority_queue import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self, contents=()):
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            self._heapify()  # Bottom-up construction of heap

    def __len__(self):
        return len(self._data)

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = smallest_child = self._left(j)
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    smallest_child = right
            if self._data[smallest_child] < self._data[j]:
                self._swap(smallest_child, j)
                self._downheap(smallest_child)

    def _heapify(self):
        parent = self._parent(len(self._data) - 1)
        for i in range(parent, -1, -1):
            self._downheap(i)

    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item._key, item._value)


class HeapSort:
    @staticmethod
    def sort(arr):
        n = len(arr)
        HeapSort._heapify(arr)
        for i in range(1, n):
            HeapSort._swap(arr, 0, n - i)
            HeapSort._downheap(arr, 0, n - i)

    @staticmethod
    def _swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    @staticmethod
    def _heapify(arr):
        n = len(arr)
        parent = (n - 1) // 2
        for i in range(parent, -1, -1):
            HeapSort._downheap(arr, i, n)

    @staticmethod
    def _downheap(arr, i, j):
        if (2 * i + 1) < j:
            child = left = 2 * i + 1
            if (2 * i + 2) < j:
                right = 2 * i + 2
                if arr[right] < arr[left]:
                    child = right
            if arr[child] < arr[i]:
                HeapSort._swap(arr, i, child)
                HeapSort._downheap(arr, child, j)

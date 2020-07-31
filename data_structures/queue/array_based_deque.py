"""
ArrayDeque : Array based double-ended queue. It is a dynamic list
that can be expanded or shrink from both sides (front and back).
"""


import ctypes


__author__ = "{Imad Dabbura}"


class Empty(Exception):
    pass


class ArrayDeque:
    """Implementation of Double-Ended Queues (Deque) using Resized Arrays."""

    def __init__(self, size=1):
        """Create an empty deque."""
        self._size = 0
        self._capacity = size
        self._data = self._make_array(self._capacity)
        self._first = 0
        self._last = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return the first element of the deque."""
        if self.is_empty():
            raise Empty("Empty Dequeue")
        return self._data[self._first]

    def last(self):
        """Return the last element of the deque."""
        if self.is_empty():
            raise Empty("Empty Dequeue")
        return self._data[self._last]

    def add_first(self, e):
        """Add element to the front of the deque."""
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._first = (self._first - 1) % self._capacity
        self._data[self._first] = e
        self._size += 1

    def add_last(self, e):
        """Add element to the back of the deque."""
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._last = (self._last + 1) % self._capacity
        self._data[self._last] = e
        self._size += 1

    def remove_first(self):
        """Remove and return the first element from the deque."""
        if self.is_empty():
            raise Empty("Empty Dequeue")
        e = self._data[self._first]
        self._data[self._first] = None
        self._first = (self._first + 1) % self._capacity
        self._size -= 1
        if 0 < self._size == self._capacity // 4:
            self._resize(self._capacity // 2)
        return e

    def remove_last(self):
        """Remove and return the last element from the deque."""
        if self.is_empty():
            raise Empty("Empty Dequeue")
        e = self._data[self._last]
        self._data[self._last] = None
        self._last = (self._last - 1) % self._capacity
        self._size -= 1
        if 0 < self._size == self._capacity // 4:
            self._resize(self._capacity // 2)
        return e

    def get(self, i):
        """Get the element at index i; otherwise return None"""
        if self._size == 0 or i >= self._size:
            return
        e = self._data[(self._first + i) % self._capacity]
        return e

    def __iter__(self):
        self._position = 0
        return self

    def __next__(self):
        """Returns the next element in the deque or raise StopIteration error."""
        if self._position == self._size:
            raise StopIteration()
        e = self._data[(self._position + self._first) % self._capacity]
        self._position += 1
        return e

    def _resize(self, capacity):
        """Resize internal array to new capacity c."""
        B = self._make_array(capacity)
        for i in range(self._size):
            B[i] = self._data[(self._first + i) % self._capacity]
        self._data = B
        self._capacity = capacity
        self._first = 0
        self._last = self._size - 1

    def _make_array(self, capacity):
        """Return an empty array with capacity c."""
        return (capacity * ctypes.py_object)()

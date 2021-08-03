"""
Queue : Implementations of generic Queue data structure. It is based on
Arrays. This implementation fulfills the optimal design for a data
structure:
- The space is proportional to the size of the collections.
- The time per operation is (almost) independent of the size of the
collections.
"""


import ctypes


__author__ = "{Imad Dabbura}"


class Empty(Exception):
    pass


class ResizedArrayQueue:
    """FIFO Queue implementation using low level resized arrays."""

    def __init__(self, size=1):
        """Create an empty queue."""
        self._data = self._make_array(size)
        self._size = 0
        self._capacity = size
        self._first = 0
        self._last = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def enqueue(self, e):
        """Add an element to the end of the queue."""
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        self._data[self._last] = e
        self._size += 1
        self._last = (self._last + 1) % self._capacity

    def dequeue(self):
        """Remove and return the element from the beginning of the queue."""
        if self.is_empty():
            raise Empty("queue underflow.")

        e = self._data[self._first]
        self._data[self._first] = None
        self._size -= 1
        self._first = (self._first + 1) % self._capacity

        if 0 < self._size == self._capacity // 4:
            self._resize(self._capacity // 2)
        return e

    def first(self):
        """Return the first element of the queue."""
        if self.is_empty():
            raise Empty("queue underflow.")
        return self._data[self._first]

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def reverse(self):
        if self._size <= 1:
            return
        for i in range(self._size // 2):
            first = (self._first + i) % self._capacity
            last = (self._last - i) % self._capacity
            self._data[first], self._data[last] = (
                self._data[last],
                self._data[first],
            )

    def __iter__(self):
        """Return the class itself as an iterator."""
        self._position = 0
        return self

    def __next__(self):
        """Returns the next element in the queue or raise StopIteration error."""
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
        self._last = self._size

    def _make_array(self, capacity):
        """Return an empty array with capacity c."""
        return (capacity * ctypes.py_object)()

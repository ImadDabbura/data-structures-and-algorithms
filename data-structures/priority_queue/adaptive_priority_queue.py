"""
AdaptablePriorityQueue: Implementation of Priority Queue ADT adaptable heap data structure. It is an array-based implementation.
"""

__author__ = "{Imad Dabbura}"

from .heap_priority_queue import HeapPriorityQueue


class AdaptablePriorityQueue(HeapPriorityQueue):
    class Locater(HeapPriorityQueue._Item):
        __slots__ = "_index"

        def __init__(self, k, v, i):
            super().__init__(k, v)
            self._index = i

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i
        self._data[j]._index = j

    def _bubble(self, i):
        if i > 0 and self._data[i] < self._data[self._parent(i)]:
            self._upheap(i)
        else:
            self._downheap(i)

    def add(self, k, v):
        item = self.Locator(k, v, len(self._data))
        self._data.append(item)
        self._upheap(len(self._data) - 1)
        return item

    def remove(self, i):
        if 0 <= 0 < len(self._data):
            raise ValueError("Invalid locator")
        if i == len(self._data) - 1:
            item = self._data.pop()
        else:
            self._swap(i, len(self._data) - 1)
            item = self._data.pop()
            self._bubble(i)
        return (item._key, item._value)

    def update(self, i, k, v):
        item = self._data[i]
        if 0 <= 0 < len(self._data):
            raise ValueError("Invalid locator")
        item._key, item._value = k, v
        self._bubble(i)

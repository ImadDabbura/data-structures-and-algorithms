"""
PriorityQueue: Implementation of Priority Queue ADT adaptable Sorted/Unsorted List data structure. It is an array-based implementation.
"""
from .positional_doubly_linked_list import PositionalList


class PriorityQueueBase:
    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __lt__(self, other):
            return self._key < other._key

    def is_empty(self):
        return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        item = self._Item(key, value)
        self._data.add_last(item)

    def _find_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        smallest = self._data.first()
        walk = self._data.after(smallest)
        while walk:
            if walk.element() < smallest.element():
                smallest = walk
            walk = self._data.after(walk)
        return smallest

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = p.element()
        self._data.delete(p)
        return (item._key, item._value)


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        walk = self._data.last()
        new = self._Item(key, value)
        while walk:
            if new >= walk.element():
                break
            walk = self._data.before(walk)
        if not walk:
            self._data.first(new)
        else:
            self._data.add_after(walk, new)

    def min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        item = self._data.first()
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("Priority queue is empty")
        p = self._data.first()
        item = self._data.delete(p)
        return (item._key, item._value)

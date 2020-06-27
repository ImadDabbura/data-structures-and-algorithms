"""
Implementation of sorted map using hash table.
"""
from .hash_table import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table."""

    def __init__(self):
        self._table = []

    def _find_index(self, k, low, high):
        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if self._table[mid]._key < k:
                return self._find_index(k, mid + 1, high)
            elif self._table[mid] > k:
                return self._find_index(k, low, mid - 1)
            else:
                return mid

    def __len__(self):
        return len(self._table)

    def __getitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError(f"KeyError: '{k}'")
        return self._table[j]._value

    def __setitem__(self, k, v):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError(f"KeyError: '{k}'")
        self._table.pop(j)

    def find_min(self, k):
        if len(self._table) == 0:
            return None
        return self._table[0]._key, self._table[0]._value

    def find_max(self):
        if len(self._table) == 0:
            return None
        return self._table[-1]._key, self._table[-1]._value

    def find_ge(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table):
            return None
        return self._table[j]._key, self._table[j]._value

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == 0:
            return None
        return self._table[j - 1]._key, self._table[j - 1]._value

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            j += 1
        if j < len(self._table):
            return self._table[j]._key, self._table[j]._value
        return None

    def find_range(self, start, stop):
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1)
        while j < len(self._table) and (
            stop is None or self._table[j]._key < stop
        ):
            yield self._table[j]._key, self._table[j]._value
            j += 1

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in self._table[::-1]:
            yield item._key

"""
Implementation os Set using Hash table.
"""
from collections.abc import MutableSet
from random import randrange


class HashMutableSet(MutableSet):
    """Set using hash map (linear probing) ADT."""

    _AVAIL = object()

    def __init__(self):
        self._table = [None] * 11
        self._n = 0
        self._prime = 109345121
        self._scale = randrange(1, self._prime)
        self._shift = randrange(self._prime)

    def _hash_function(self, e):
        return (
            (hash(e) * self._scale + self._shift)
            % self._prime
            % len(self._table)
        )

    def _resize(self, capacity):
        old_list = list(self._table)
        self._n = 0
        self._table = [None] * capacity
        for i, e in enumerate(old_list):
            if not (e is None or e is HashMutableSet._AVAIL):
                self.add(e)

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is HashMutableSet._AVAIL

    def _find_slot(self, j, e):
        first_available = None
        while True:
            if self._is_available(j):
                if first_available is None:
                    first_available = j
                if self._table[j] is None:
                    return False, j
            elif self._table[j] == e:
                return True, j
            j = (j + 1) % len(self._table)

    def add(self, e):
        j = self._hash_function(e)
        found, s = self._find_slot(j, e)
        if found:
            return
        self._table[s] = e
        self._n += 1
        if self._n > len(self._table) // 2:
            self._resize(len(self._table) * 2 - 1)

    def discard(self, e):
        j = self._hash_function(e)
        found, s = self._find_slot(j, e)
        if found:
            self._table[s] = HashMutableSet._AVAIL
            self._n += 1

    def __contains__(self, e):
        j = self._hash_function(e)
        found, s = self._find_slot(j, e)
        if found:
            return True
        return False

    def __len__(self):
        return self._n

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]

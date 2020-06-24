from collections.abc import MutableMapping
from random import randrange


class MapBase(MutableMapping):
    """Abstract base class that implements map items."""

    class _Item:
        """Class that will store map items as key-value pairs."""

        __slots__ = "_key", "_value"

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key


class UnsortedTableMap(MapBase):
    """Map implementation using unsorted list (array)."""

    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        for item in self._table:
            if item._key == key:
                return item._value
        raise KeyError(f"KeyError: '{key}'")

    def __setitem__(self, key, value):
        for item in self._table:
            if item._key == key:
                item._value = value
                return
        self._table.append(self._Item(key, value))

    def __delitem__(self, k):
        for i, item in enumerate(self._table):
            if item._key == k:
                self._table.pop(i)
                return
        raise KeyError(f"KeyError: '{k}'")

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key


class HashMapBase(MapBase):
    """Abstract base class for map using hash-table with MAD compression."""

    def __init__(self, capacity=11, p=109345121):
        self._table = [None] * capacity
        self._n = 0
        self._prime = p
        self._scale = randrange(1, p)
        self._shift = randrange(p)

    def _hash_function(self, k):
        return (
            (hash(k) * self._scale + self._shift)
            % self._prime
            % len(self._table)
        )

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1

    def _resize(self, capacity):
        old_table = list(self.items())
        self._table = [None] * capacity
        self._n = 0
        for k, v in old_table:
            self[k] = v


class ChainHashMap(HashMapBase):
    """Hash map implemented using separate chaining for collision resolution."""

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if not bucket:
            raise KeyError(f"KeyError: {k}")
        return bucket[k]

    def _bucket_setitem(self, j, k, v):
        bucket = self._table[j]
        if not self._table[j]:
            bucket = self._table[j] = UnsortedTableMap()
        old_size = len(bucket)
        bucket[k] = v
        if len(bucket) > old_size:
            self._n += 1

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if not bucket:
            raise KeyError(f"KeyError: {k}")
        del bucket[k]

    def __iter__(self):
        for bucket in self._table:
            if bucket:
                for key in bucket:
                    yield key


class ProbeHashMap(HashMapBase):
    """Hash map implemented using linear probing for collision resolution."""

    # used as a mark to differentiate it between a cell never been
    # occupied and a cell that was deleted
    _AVAIL = object()

    def _is_available(self, j):
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        first_available = None
        while True:
            if self._is_available(j):
                if not first_available:
                    first_available = j
                if not self._table[j]:
                    return (False, first_available)
            elif self._table[j]._key == k:
                return (True, j)
            j = (j + 1) % len(self._table)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError(f"KeyError: {k}")
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if found:
            self._table[s]._value = v
        else:
            self._table[s] = self._Item(k, v)
            self._n += 1

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError(f"KeyError: {k}")
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for i in range(len(self._table)):
            if not self._is_available(i):
                yield self._table[i]._key

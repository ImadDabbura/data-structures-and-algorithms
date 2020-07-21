import ctypes


class DynamicArray:
    """A dynamic array class similar to Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Returns the number of elements stored in the array."""
        return len(self._A)

    def __getitem__(self, i):
        """Returns the element at index i."""
        if not 0 <= i < self._n:
            raise IndexError("Invalid index")
        return self._A[i]

    def __setitem__(self, i, value):
        if not 0 <= i < self._n:
            raise IndexError("Invalid index")
        self._A[i] = value

    def append(self, obj):
        """Add object to the end of the array."""
        if self._n == self._capacity:
            self._resize(self._capacity * 2)
        self._A[self._n] = obj
        self._n += 1

    def __contains__(self, val):
        """Returns True if val in the list, False otherwise."""
        for i in range(self._n):
            if val == self._A[i]:
                return True
        return False

    def index(self, val):
        """Returns the index of val, or raise ValueError."""
        for i in range(self._n):
            if val == self._A[i]:
                return i
        raise ValueError("value not in list.")

    def count(self, val):
        """Return number of occurrences of value."""
        res = 0
        for i in range(self._n):
            if val == self._A[i]:
                res += 1
        return res

    def insert(self, k, val):
        """Insert val at index k, shifting subsequent values rightward."""
        if self._n == self._capacity:
            # Double the size of the array since it is full
            self._resize(self._capacity * 2)
        for i in range(self._n, k, -1):
            self._A[i] = self._A[i - 1]
        self._A[k] = val
        self._n += 1

    def remove(self, val):
        """Remove first occurance of val, shifting subsequent values leftward."""
        for i in range(self._n):
            if val == self._A[i]:
                for j in range(i, self._n - 1):
                    self._A[j] = self._A[i + 1]
                self._n -= 1
                self._A[self._n] = None  # Avoid loitering
                if self._n > 0 and self._n == self._capacity / 4:
                    # Half the array
                    self._resize(self._capacity * 0.5)
                return
        raise ValueError("val not found")

    def reverse(self):
        """Reverse list in place."""
        if self._n <= 1:
            return
        for i in range(self._n // 2):
            self._A[i], self._A[self._n - i - 1] = (
                self._A[self._n - i - 1],
                self._A[i],
            )

    def __iter__(self):
        """Iterator returns itself as an iterator."""
        self._pos = -1
        return self

    def __next__(self):
        """Returns the next element or raise StopIteration error."""
        self._pos += 1
        if self._pos < self._n:
            return self._A[self._pos]
        else:
            raise StopIteration()

    def _resize(self, c):
        """Resize internal array to new capacity c."""
        B = self._make_array(c)
        for i in range(self._n):
            B[i] = self._A[i]
        self._A = B
        self._capacity = c

    def _make_array(self, c):
        """Return an empty array with capacity c."""
        return (c * ctypes.py_object)()

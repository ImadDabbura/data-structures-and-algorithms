"""
Basic implementation of deques using Doubly Linked List.
"""


__author__ = "{Imad Dabbura}

class Empty(Exception):
    pass


class _DLListBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        __slots__ = "_element", "_prev", "_next"

        def __init__(self, element, prev_node, next_node):
            self._element = element
            self._next = next_node
            self._prev = prev_node

    def __init__(self):
        self._size = 0
        self._sentinel_front = self._Node(None, None, None)
        self._sentinel_back = self._Node(None, None, None)
        self._sentinel_front._next = self._sentinel_back
        self._sentinel_back._prev = self._sentinel_front

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, prev_node, next_node):
        "Add element e between two existing nodes."
        new_node = self._Node(e, prev_node, next_node)
        prev_node._next = new_node
        next_node._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        "Delete nonsentinel node and return its element."
        prev_node = node._prev
        next_node = node._next
        e = node._element
        prev_node._next = next_node
        next_node._prev = prev_node
        self._size -= 1
        node._prev = node._next = node._element = None
        return e


class DLListDeque(_DLListBase):
    """
    FIFO Queue implementation using doubly linked list as the underlying data 
    structure.
    """

    def __getitem__(self, index):
        if self.is_empty():
            raise Empty("list is empty")
        elif not 0 <= index < self._size:
            raise IndexError("index out of range")
        position = index
        current_node = self._sentinel_front
        while position >= 0:
            current_node = current_node._next
            position -= 1
        return current_node._element

    def add_first(self, element):
        self._insert_between(
            element, self._sentinel_front, self._sentinel_front._next
        )

    def add_last(self, element):
        self._insert_between(
            element, self._sentinel_back._prev, self._sentinel_back
        )

    def first(self):
        if self.is_empty():
            raise Empty("List is empty.")
        return self._sentinel_front._next._element

    def last(self):
        if self.is_empty():
            raise Empty("List is empty.")
        return self._sentinel_back._prev._element

    def remove_first(self):
        if self.is_empty():
            raise Empty("list is empty.")
        _ = self._delete_node(self._sentinel_front._next)

    def remove_last(self):
        if self.is_empty():
            raise Empty("list is empty.")
        _ = self._delete_node(self._sentinel_back._prev)

    def __iter__(self):
        self._current_node = self._sentinel_front._next
        return self

    def __next__(self):
        while not self._current_node._next:
            raise StopIteration()
        e = self._current_node._element
        self._current_node = self._current_node._next
        return e


class _CircularDLListBase(_DLListBase):
    """A base class providing a circular doubly linked list representation."""

    def __init__(self):
        self._size = 0
        self._sentinel = self._Node(None, None, None)
        self._sentinel._prev = self._sentinel
        self._sentinel._next = self._sentinel


class CircularDLListDeque(_CircularDLListBase):
    """
    FIFO Queue implementation using circular doubly linked list as the 
    underlying data structure.
    """

    def __getitem__(self, index):
        if self.is_empty():
            raise Empty("list is empty")
        elif not 0 <= index < self._size:
            raise IndexError("index out of range")
        position = index
        current_node = self._sentinel
        while position >= 0:
            current_node = current_node._next
            position -= 1
        return current_node._element

    def add_first(self, element):
        self._insert_between(element, self._sentinel, self._sentinel._next)

    def add_last(self, element):
        self._insert_between(element, self._sentinel._prev, self._sentinel)

    def first(self):
        if self.is_empty():
            raise Empty("List is empty.")
        return self._sentinel._next._element

    def last(self):
        if self.is_empty():
            raise Empty("List is empty.")
        return self._sentinel._prev._element

    def remove_first(self):
        if self.is_empty():
            raise Empty("list is empty.")
        _ = self._delete_node(self._sentinel._next)

    def remove_last(self):
        if self.is_empty():
            raise Empty("list is empty.")
        _ = self._delete_node(self._sentinel._prev)

    def __iter__(self):
        self._current_node = self._sentinel._next
        self._counter = 0
        return self

    def __next__(self):
        if self._counter == self._size:
            raise StopIteration()
        e = self._current_node._element
        self._current_node = self._current_node._next
        self._counter += 1
        return e

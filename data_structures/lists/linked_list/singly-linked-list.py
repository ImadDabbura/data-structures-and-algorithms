"""
Basic implementation of python list using Singly Linked List.
"""


__author__ = "{Imad Dabbura}"


class Empty(Exception):
    pass


class SLList:
    """List of objects using Singly Linked List data structure."""

    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node

    def __init__(self):
        self._size = 0
        self._sentinel = self._Node(None, None)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if self._size == 0:
            raise IndexError("list is empty.")
        if not 0 <= index < self._size:
            raise IndexError("index out of range")
        current_node = self._sentinel
        position = index
        while position >= 0:
            current_node = current_node._next
            position -= 1
        return current_node._element

    def __setitem__(self, index, value):
        if not 0 <= index < self._size:
            raise IndexError("Invalid out of range")
        current_node = self._sentinel
        position = index
        while position >= 0:
            current_node = current_node._next
            position -= 1
        current_node._element = value

    def add_first(self, element):
        new_node = self._Node(element, self._sentinel._next)
        self._sentinel._next = new_node
        self._size += 1

    def add_last(self, element):
        current_node = self._sentinel
        while current_node._next:
            current_node = current_node._next
        new_node = self._Node(element, None)
        current_node._next = new_node
        self._size += 1

    def get_first(self):
        if self._size == 0:
            raise Empty("List is empty.")
        return self._sentinel._next._element

    def get_last(self):
        if self._size == 0:
            raise Empty("List is empty.")
        current_node = self._sentinel._next
        while current_node:
            current_node = current_node._next
        return current_node._element

    def insert(self, e, position):
        if position == 0:
            self.add_first(e)
        elif position >= self._size:
            self.add_last(e)
        else:
            current_node = self._sentinel._next
            while position > 1:
                current_node = current_node._next
                position -= 1
            new_Node = self._Node(e, current_node._next)
            current_node._next = new_Node
        self._size += 1

    def remove_first(self):
        if self._size == 0:
            raise Empty("List is empty.")
        tmp = self._sentinel._next
        self._sentinel._next = self._sentinel._next._next
        tmp = None
        self._size -= 1

    def remove_last(self):
        if self._size == 0:
            raise Empty("List is empty.")
        current_node = self._sentinel
        while current_node._next._next:
            current_node = current_node._next
        tmp = current_node._next
        current_node._next = None
        tmp = None
        self._size -= 1

    def remove(self, e):
        if self._size == 0:
            raise Empty("List is empty.")
        current_node = self._sentinel
        while current_node._next:
            if current_node._next._element == e:
                current_node._next = current_node._next._next
                self._size -= 1
                return
            current_node = current_node._next
        raise ValueError(f"{e} not in list")

    def __contains__(self, e):
        if self._size == 0:
            raise Empty("List is empty.")
        current_node = self._sentinel._next
        while current_node:
            if current_node._element == e:
                return True
            current_node = current_node._next
        return False

    def count(self, e):
        if self._size == 0:
            raise Empty("List is empty.")
        total = 0
        current_node = self._sentinel._next
        while current_node:
            if current_node._element == e:
                total += 1
            current_node = current_node._next
        return total

    def reverse(self):
        if self._size <= 1:
            return
        current_node = self._sentinel._next._next
        self._sentinel._next._next = None
        while current_node:
            tmp = current_node._next
            current_node._next = self._sentinel._next
            self._sentinel._next = current_node
            current_node = tmp

    def __iter__(self):
        self._current_node = self._sentinel._next
        return self

    def __next__(self):
        if not self._current_node:
            raise StopIteration()
        e = self._current_node._element
        self._current_node = self._current_node._next
        return e

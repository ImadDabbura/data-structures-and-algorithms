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


class PositionalList(_DLListBase):
    """A sequential container of elements allowing positional access."""

    class Position:
        "An abstraction that represent the location of a node."

        def __init__(self, container, node):
            """
            container : List
                the list that contains the node.
            node : Node
                node representing one element in the list.
            """
            self._container = container
            self._node = node

        def element(self):
            """Returns the element stored in this position."""
            return self._node._element

        def __eq__(self, other):
            """Returns True if other represents the same position (node) in the list."""
            return type(self) == type(other) and self._node is other._node

        def __ne__(self, other):
            """Returns True if other does not represent the same position (node) in the list."""
            return not (self == other)

    def _validate(self, p):
        """Return position's p nonde, or raise error if the node is invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type.")
        if p._container is not self:
            raise ValueError("p does not belong to this container.")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance of a given node, None if its sentinel node."""
        if node is self._sentinel_front or node is self._sentinel_back:
            return None
        return self.Position(self, node)

    def first(self):
        """Returns first position, or None if list is empty."""
        return self._make_position(self._sentinel_front._next)

    def last(self):
        """Returns last position, or None if list is empty."""
        return self._make_position(self._sentinel_back._prev)

    def before(self, p):
        """Returns previous position of p, or None if p is first position."""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """Returns position after after p, or None if p is last position."""
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        position = self.first()
        while position:
            yield position.element
            position = self.after(position)

    def _insert_between(self, e, prev_node, next_node):
        node = super()._insert_between(e, prev_node, next_node)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(
            e, self._sentinel_front, self._sentinel_front._next
        )

    def add_last(self, e):
        return self._insert_between(
            e, self._sentinel_back._prev, self._sentinel_back
        )

    def add_before(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)

    def add_after(self, p, e):
        node = self._validate(p)
        return self._insert_between(e, node, node._next)

    def delete(self, p):
        node = self._validate(p)
        return self._delete_node(node)

    def replace(self, p, e):
        node = self._validate(p)
        old_element = node._element
        node._element = e
        return old_element


def insetion_sort(L):
    """Sort Positional list in a nondecreasing order."""
    if len(L) > 1:
        largest = L.first()
        while largest != L.last():
            pivot = L.after(largest)
            value = pivot.element()
            if value > largest:
                largest = value
            else:
                walk = largest
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)

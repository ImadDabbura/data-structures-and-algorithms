from ..stacks.linked_list_based_stack import LinkedListStack


class Empty(Exception):
    pass


class LinkedListQueue:
    """FIFO Queue implementation using singly linked list as the underlying data structure."""

    class _Node:
        """Nested class that implements the linkedlist data structure."""

        __slots__ = "_element", "_next"

        def __init__(self, element, node):
            self._element = element
            self._next = node

    def __init__(self, size=1):
        """Create an empty queue."""
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def enqueue(self, e):
        """Add an element to the end of the queue."""
        new_node = self._Node(e, None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the element from the beginning of the queue."""
        if self.is_empty():
            raise Empty("Queue underflow.")
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return element

    def first(self):
        """Return the first element of the queue."""
        if self.is_empty():
            raise Empty("Queue undeflow.")
        return self._head._element

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def reverse(self):
        """Non-destrucive reverse. Returns new instance of Queue with reversed element."""
        Q = LinkedListQueue()
        S = LinkedListStack()
        current_node = self._head

        while current_node:
            S.push(current_node._element)
            current_node = current_node._next

        while not S.is_empty():
            Q.enqueue(S.pop())

        return Q

    def __iter__(self):
        """Return the class itself as an iterator."""
        self._current_node = self._head
        return self

    def __next__(self):
        """Returns the next element in the queue or raise StopIteration error."""
        if not self._current_node:
            raise StopIteration()
        element = self._current_node._element
        self._current_node = self._current_node._next
        return element


class CircularLinkedListQueue:
    """FIFO Queue implementation using circularly linked list as the underlying data structure."""

    class _Node:
        """Nested class that implements the linkedlist data structure."""

        __slots__ = "_element", "_next"

        def __init__(self, element, node):
            self._element = element
            self._next = node

    def __init__(self, size=1):
        """Create an empty queue."""
        self._tail = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def enqueue(self, e):
        """Add an element to the end of the queue."""
        new_node = self._Node(e, None)
        if self.is_empty():
            new_node._next = new_node
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """Remove and return the element from the beginning of the queue."""
        if self.is_empty():
            raise Empty("Queue underflow.")
        head = self._tail._next
        element = head._element
        self._size -= 1
        if self.is_empty():
            self._tail = None
        else:
            self._tail._next = head._next
        return element

    def first(self):
        """Return the first element of the queue."""
        if self.is_empty():
            raise Empty("Queue is empty.")
        head = self._tail._next
        return head._element

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 1:
            self._tail = self._tail._next

    def __iter__(self):
        """Return the class itself as an iterator."""
        self._current_node = self._tail._next
        self._counter = 0
        return self

    def __next__(self):
        """Returns the next element in the queue or raise StopIteration error."""
        if self._counter >= self._size:
            raise StopIteration()
        element = self._current_node._element
        self._current_node = self._current_node._next
        self._counter += 1
        return element

'''
Dequeue : Implementations of generic double-ended queue data structure. It is 
based on Doubly Linked List. This implementation fulfills the optimal design 
for a data structure:
- The space is proportional to the size of the collections.
- Insertion/deltion on both ends are O(1). However, interior deletion is not
O(1).
'''


__author__ = '{Imad Dabbura}'


class Empty(Exception):
    pass


class DoublyLinkedDeque:
    '''
    Implementation of Double-Ended Queues (Deque) using doubly linked
    list as the underlying data structure.
    '''
    
    class _Node:
        '''Nested class that implements the doubly linkedlist data structure.'''
        __slots__ = '_prev', '_element', '_next'
        
        def __init__(self, element, prev_node, next_node):
            self._element = element
            self._prev = prev_node
            self._next = next_node

    def __init__(self):
        '''Create an empty deque.'''
        self._size = 0
        self._sentinel_front = self._Node(None, None, None)
        self._sentinel_back = self._Node(None, None, None)
        self._sentinel_front._next = self._sentinel_back
        self._sentinel_back._prev = self._sentinel_front

    def __len__(self):
        '''Return the number of elements in the queue.'''
        return self._size

    def is_empty(self):
        '''Return True if the queue is empty.'''
        return self._size == 0

    def first(self):
        '''Return the first element of the deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')
        head = self._sentinel_front._next
        return head._element

    def last(self):
        '''Return the last element of the deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')
        tail = self._sentinel_back._prev
        return tail._element
    
    def add_first(self, e):
        '''Add element to the front of the deque.'''
        self._sentinel_front._next = self._Node(e, self._sentinel_front, self._sentinel_front._next)
        self._sentinel_front._next._next._prev = self._sentinel_front._next
        self._size += 1
    
    def add_last(self, e):
        '''Add element to the back of the deque.'''
        self._sentinel_back._prev._next = self._Node(e, self._sentinel_back._prev, self._sentinel_back)
        self._sentinel_back._prev = self._sentinel_back._prev._next
        self._size += 1

    def remove_first(self):
        '''Remove and return the first element from the deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')
        self._sentinel_front._next = self._sentinel_front._next._next
        self._sentinel_front._next._prev = self._sentinel_front
        self._size -= 1

    def remove_last(self):
        '''Remove and return the last element from the deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')
        self._sentinel_back._prev = self._sentinel_back._prev._prev
        self._sentinel_back._prev._next = self._sentinel_back
        self._size -= 1

    def get(self, i):
        '''Get the element at index i; otherwise return None'''
        if self._size == 0 or i >= self._size:
            return
        
        current_node = self._sentinel_front._next
        for _ in range(i):
            current_node = current_node._next
        return current_node._element
    
    def __iter__(self):
        '''Return the class itself as an iterator.'''
        self._current_node = self._sentinel_front._next
        self._position = 0
        return self
    
    def __next__(self):
        '''Return next element in the deque or raise StopIteration error.'''
        if self._position == self._size:
            raise StopIteration()
        
        element = self._current_node._element
        self._current_node = self._current_node._next
        self._position += 1
        return element
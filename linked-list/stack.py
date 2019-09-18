'''
Stack : Implementations of generic Stack data structure. It is based on
Singly linked list. This implementation fulfills the optimal design for a data
structure:
- The space is proportional to the size of the collections.
- All main operations are O(1).
'''

__author__ = '{Imad Dabbura}'


class Empty(Exception):
    pass


class LinkedStack:
    '''LIFO Stack implementation using singly linked list as the underlying data structure.'''
    
    class _Node:
        '''Nested class that implements the linkedlist data structure.'''
        __slots__ = '_element', '_next'
        
        def __init__(self, element, node):
            self._element = element
            self._next = node
    
    def __init__(self):
        '''Create an empty stack.'''
        self._size = 0
        self._head = None
    
    def __len__(self):
        '''Return the number of elements in the stack.'''
        return self._size
    
    def push(self, e):
        '''Add an element to the top of the stack.'''
        self._head = self._Node(e, self._head)
        self._size += 1
    
    def pop(self):
        '''Remove and return the element from the top of the stack.'''
        if self.is_empty():
            raise Empty('Stack is empty.')
        element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return element

    def top(self):
        '''Return the top element of the stack.'''
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._head._element
    
    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0
    
    def reverse(self):
        '''Non-destrucive reverse. Returns new instance of Queue with reversed element.'''
        S = LinkedStack()
        current_node = self._head
        
        while current_node:
            S.push(current_node._element)
            current_node = current_node._next
        
        return S
    
    def __iter__(self):
        '''Return the class itself as an iterator.'''
        self._current_node = self._head
        return self
    
    def __next__(self):
        '''Returns the next element in the stack or raise StopIteration error.'''
        if not self._current_node:
            raise StopIteration()

        element = self._current_node._element
        self._current_node = self._current_node._next
        return element

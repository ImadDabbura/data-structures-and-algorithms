'''
Stack : Implementations of generic Stack data structure. It is based on
Arrays. This implementation fulfills the optimal design for a data
structure:
- The space is proportional to the size of the collections.
- The time per operation is (almost) independent of the size of the
collections.
'''


import ctypes


__author__ = '{Imad Dabbura}'


class Empty(Exception):
    pass


class ResizedArrayStack:
    '''LIFO Stack implementation using low level resized arrays.'''
    
    def __init__(self, size=1):
        '''Create an empty stack.'''
        self._data = self._make_array(size)
        self._size = 0
        self._capacity = size
    
    def __len__(self):
        '''Return the number of elements in the stack.'''
        return self._size
    
    def push(self, e):
        '''Add an element to the top of the stack.'''
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = e
        self._size += 1
    
    def pop(self):
        '''Remove and return the element from the top of the stack.'''
        if self.is_empty():
            raise Empty('Stack is empty.')
        e = self._data[self._size - 1]
        self._data[self._size -1] = None
        self._size -= 1
        if 0 < self._size == self._capacity / 4:
            self._resize(self._capacity // 2)
        return e

    def top(self):
        '''Return the top element of the stack.'''
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._data[self._size - 1]
    
    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0
    
    def reverse(self):
        if self._size <= 1:
            return
        for i in range(self._size // 2):
            self._data[i], self._data[self._size - i - 1] = (self._data[self._size - i - 1],
                                                             self._data[i])
    
    def __iter__(self):
        '''Return the class itself as an iterator.'''
        self._position = self._size
        return self
    
    def __next__(self):
        '''Returns the next element in the stack or raise StopIteration error.'''
        if self._position == 0:
            raise StopIteration()
        e = self._data[self._position - 1]
        self._position -= 1
        return e

    def _resize(self, capacity):
        '''Resize internal array to new capacity c.'''
        B = self._make_array(capacity)
        for i in range(self._size):
            B[i] = self._data[i]
        self._data = B
        self._capacity = capacity
    
    def _make_array(self, capacity):
        '''Return an empty array with capacity c.'''
        return (capacity * ctypes.py_object)()

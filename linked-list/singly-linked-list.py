'''
Basic implementation of python list using Singly Linked List.
'''


__author__ = '{Imad Dabbura}'


class Empty(Exception):
    pass


class SLList:
    '''List of objects using Singly Linked List data structure.'''

    class _Node:
        '''Nested class that implements the doubly linkedlist data structure.'''
        __slots__ = '_element', '_next'
        
        def __init__(self, element, next_node):
            self._element = element
            self._next = next_node
    
    def __init__(self):
        self._size = 0
        self._sentinel = self._Node(None, None)
    
    def __len__(self):
        return self._size
    
    def add_first(self, e):
        '''Add element e at the head of the list.'''
        self._sentinel._next = self._Node(e, self._sentinel._next)
        self._size += 1
    
    def add_last(self, e):
        '''Add element e to the tail of the list.'''
        current_node = self._sentinel
        while current_node._next is not None:
            current_node = current_node._next
        
        current_node._next = self._Node(e, None)
        self._size += 1

    def get_first(self):
        '''Get the first element.'''
        if self._size == 0:
            raise Empty('List is empty.')
        return self._sentinel._next._element
        
    def get_last(self):
        '''Get the last element.'''
        if self._size == 0:
            raise Empty('List is empty.')
        
        current_node = self._sentinel
        while current_node._next is not None:
            current_node = current_node._next
        return current_node._element
    
    def insert(self, e, position):
        '''Insert the element at index position; otherwise insert at index len(l).'''
        if position == 0 or self._size == 0:
            self.add_first(e)
        elif position >= self._size:
            self.add_last(e)
        else:
            current_node = self._sentinel._next
            while position > 1 and current_node._next is not None:
                current_node = current_node._next
                position -= 1
            current_node._next = self._Node(e, current_node._next)
            self._size += 1

    def remove_first(self):
        '''Remove the first element.'''        
        if self._size == 0:
            raise Empty('List is empty.')
        self._sentinel._next = self._sentinel._next._next
        self._size -= 1

    def remove_last(self):
        '''Remove the last element.'''
        if self._size == 0:
            raise Empty('List is empty.')
        
        current_node = self._sentinel
        while current_node._next._next is not None:
            current_node = current_node._next
        current_node._next = None
        self._size -= 1

    def remove(self, e):
        '''
        Remove element the first occurance of element e from the list; otherwise,
        raise ValueError.
        '''
        if self._size == 0:
            raise Empty('List is empty.')
        current_node = self._sentinel
        while current_node._next is not None:
            if current_node._next._element == e:
                current_node._next = current_node._next._next
                self._size -= 1
                return
            current_node = current_node._next
        raise ValueError(f'{e} not in list.')
    
    def __contain__(self, e):
        if self._size == 0:
            raise Empty('List is empty.')
        current_node = self._sentinel._next
        while current_node is not None:
            if current_node._element == e:
                return True
            current_node = current_node._next
        return False
    
    def count(self, e):
        '''Return the number of occurance of element e.'''
        if self._size == 0:
            raise Empty('List is empty.')
        ans = 0
        current_node = self._sentinel._next
        while current_node is not None:
            if current_node._element == e:
                ans += 1
            current_node = current_node._next
        return ans

    def get(self, i):
        '''Get the element at index i; otherwise return the element if i >= len(l).'''
        if self._size == 0:
            raise Empty('List is empty.')
        current_node = self._sentinel._next
        while i > 0 and current_node._next is not None:
            current_node = current_node._next
            i -= 1
        return current_node._element
    
    def reverse(self):
        '''Reverse the list in-place.'''
        if self._size <= 1:
            return
        current_node = self._sentinel._next._next
        self._sentinel._next._next = None
        while current_node is not None:
            temp = current_node._next
            current_node._next = self._sentinel._next
            self._sentinel._next = current_node
            current_node = temp
    
    def __iter__(self):
        '''Return the class itself as an iterator.'''
        self._current_node = self._sentinel._next
        return self
    
    def __next__(self):
        '''Return next element in the list or raise StopIteration error.'''
        if self._current_node is None:
            raise StopIteration()
        e = self._current_node._element
        self._current_node = self._current_node._next
        return e

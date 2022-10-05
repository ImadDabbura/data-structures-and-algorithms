"""
Tree: Implementation of ADT for general tree data structure. All trees should 
inherit from this class. It is a linked list implementation of tree.
"""

__author__ = "{Imad Dabbura}"

from queue import Queue


class Tree:
    """Abstract base class representing a tree structure."""

    class Position:
        """An abstraction representing the location of a single element."""

        def element(self):
            """Return the element stored at this Position."""
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            """Return True if other Position represents the same location."""
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

    def root(self):
        """Return Position representing the tree's root (or None if empty)."""
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        """Return Position representing p's parent (or None if p is root)."""
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        raise NotImplementedError("must be implemented by subclass")

    def len(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        """Return True if Position p represents the root of the tree."""
        return self.root() == p

    def is_leaf(self, p):
        """Return True if Position p does not have any children."""
        return self.num_children(p) == 0

    def is_empty(self):
        """Return True if the tree is empty."""
        return len(self) == 0

    def depth(self, p):
        """Return the depth of position p."""
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of tree."""
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of subtree at position p."""
        if self.is_leaf(p):
            return 0
        return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """
        Return the height of subtree at position p. If p is None, returns the
        height of the tree at the root.
        """
        if not p:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        """Generate an iteration of all elements in the tree."""
        for p in self.positions():
            yield p.element()

    def _preorder(self, p):
        """Generate a preorder iteration of all positions in a subtree rooted at p."""
        yield p
        for c in self.children(p):
            for other in self._preorder(c):
                yield other

    def preorder(self):
        """Generate a preorder iteration of positions in tree."""
        if not self.is_empty():
            for p in self._preorder(self.root()):
                yield p

    def _postorder(self, p):
        """Generate a postorder iteration of all positions in a subtree rooted at p."""
        for c in self.children(p):
            for other in self._postorder(c):
                yield other
        yield p

    def postorder(self):
        """Generate a postorder iteration of positions in tree."""
        if not self.is_empty():
            for p in self._postorder(self.root()):
                yield p

    def breadth_first(self):
        """Generate breadth-first iteration of positions in tree."""
        if not self.is_empty():
            q = Queue()
            q.put(self.root())
            while not q.empty():
                p = q.get()
                yield p
                for c in self.children(p):
                    q.put(c)

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.preorder()

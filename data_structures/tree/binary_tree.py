"""
BinaryTree: Implementation of ADT for binary tree data structure. All binary trees should 
inherit from this class. It is a linked list implementation of tree.
"""

__author__ = "{Imad Dabbura}"
from .tree import Tree


class BinaryTree(Tree):
    """Abstract base class representing a binary tree structure."""

    def left(self, p):
        """
        Return a Position representing p's left child, or None if p does not have a left child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def right(self, p):
        """
        Return a Position representing p's right child, or None if p does not have a right child.
        """
        raise NotImplementedError("must be implemented by subclass")

    def sibling(self, p):
        """Return a Position representing p s sibling (or None if no sibling)."""
        parent = self.parent(p)
        if parent is None:  # root node has no parent/sibling
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            return self.left(parent)

    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        if self.left(p):
            yield self.left(p)
        if self.right(p):
            yield self.right(p)

    def _inorder(self, p):
        """Generate inorder iteration of positions in a subtree rooted at p."""
        if self.left(p):
            for other in self._inorder(self.left(p)):
                yield other
        yield p
        if self.right(p):
            for other in self._inorder(self.right(p)):
                yield other

    def inorder(self):
        """Generate inorder iteration of positions in the tree."""
        if not self.is_empty():
            for p in self._inorder(self.root()):
                yield p

    def positions(self):
        """Generate an iteration of the tree's positions."""
        return self.inorder()


class LinkedBinaryTree(BinaryTree):
    """Linked representation of binary tree."""

    class _Node:
        __slots__ = "_parent", "_left", "_right", "_element"

        def __init__(self, parent, left, right, element):
            self._parent = parent
            self._left = left
            self._right = right
            self._element = element

    class Position(BinaryTree.Position):
        """An abstraction representing the position of an element (node)."""

        def __init__(self, tree, node):
            self._tree = tree
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(self) == type(other) and self._node is other._node

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError("p must be a Position type")
        elif p._tree is not self:
            raise ValueError("p does not belong to this tree")
        elif p._node._parent is p._node:
            return ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def root(self):
        return self._root

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left:
            count += 1
        if node._right:
            count += 1
        return count

    def _add_root(self, e):
        if self._root:
            raise ValueError("Root exists")
        root = self._Node(None, None, None, e)
        self._size += 1
        return self._make_position(root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left:
            raise ValueError("Left child exists")
        node._left = self._Node(node, None, None, e)
        self._size += 1
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right:
            raise ValueError("Right child exists")
        node._right = self._Node(node, None, None, e)
        self._size += 1
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old_element = node._element
        node._element = e
        return old_element

    def _delete(self, p):
        if self.num_children(p) == 2:
            raise ValueError("p has two children")
        node = self._validate(p)
        child = node._left if node._left else node._right
        if child:
            child._parent = node._parent
        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if parent._left is node:
                parent._left = child
            else:
                parent._right = child
        element = node._element
        self._size -= 1
        node._element = node._left = node._right = None
        node._parent = node
        return element

    def _attach(self, p, t1, t2):
        if not self.is_leaf(p):
            raise ValueError("p must be leaf")
        if not type(self) == type(t1) == type(t2):
            raise TypeError("Trees must be of the same type")
        node = self._validate(p)
        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2
            t2._root = None
            t2._size = 0

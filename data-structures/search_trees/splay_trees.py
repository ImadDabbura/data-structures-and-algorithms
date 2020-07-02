"""
Implementation of Sorted Map using Splay tree implementation of BST.
"""

from .bst import BinarySearchTreeMap

__author__ = "{Imad Dabbura}"


class SplayTreeMap(BinarySearchTreeMap):
    """Sorted map implementation using splay tree."""

    def _splay(self, node):
        while node is not self.root():
            parent = self.parent(node)
            grand_parent = self.parent(parent)

            # zig case
            if not grand_parent:
                self._rotate(node)

            # zig-zig case
            elif (parent == self.left(grand_parent)) == (
                node == self.left(parent)
            ):
                self._rotate(parent)
                self._rotate(node)

            # zig-zag case (similar double-rotation)
            else:
                self._rotate(node)
                self._rotate(node)

    def _rebalance_access(self, node):
        self._splay(node)

    def _rebalance_insert(self, node):
        self._splay(node)

    def _rebalance_delete(self, node):
        if node:
            self._splay(node)

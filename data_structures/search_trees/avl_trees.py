"""
Implementation of Sorted Map using AVL tree implementation of BST.
"""

from .bst import BinarySearchTreeMap

__author__ = "{Imad Dabbura}"


class AVLTreeMap(BinarySearchTreeMap):
    """Sorted map implementation using an AVL tree."""

    class _Node(BinarySearchTreeMap._Node):
        def __init__(self, parent, left, right, item):
            super().__init__(parent, left, right, item)
            self._height = 0

        def left_height(self):
            return self._left._height if self._left else 0

        def right_height(self):
            return self._right._height if self._right else 0

    def _recompute_height(self, node):
        node._height = 1 + max(node.left_height(), node.right_height())

    def _is_balanced(self, node):
        return abs(node.left_height() - node.right_height()) <= 1

    def _tall_child(self, node, favor_left=False):
        if node.left_height() + favor_left * 1 > node.right_height():
            return self.left(node)
        return self.right(node)

    def _tall_grandchild(self, node):
        child = self._tall_child(node)
        alignment = child == self.left(node)
        return self._tall_child(child, alignment)

    def _rebalance(self, node):
        current_node = node
        while current_node:
            old_height = node._height
            if not self._is_balanced(current_node):
                current_node = self._restructure(
                    self._tall_grandchild(current_node)
                )
                self._recompute_height(self.left(current_node))
                self._recompute_height(self.right(current_node))
            self._recompute_height(current_node)
            if old_height == current_node._height:
                current_node = None
            else:
                current_node = self.parent(current_node)

    def _rebalance_insert(self, node):
        return self._rebalance(node)

    def _rebalance_delete(self, node):
        return self._rebalance(node)

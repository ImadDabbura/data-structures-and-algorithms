"""
Implementation of Sorted Map using Red-Black tree implementation of BST.
"""

from .bst import BinarySearchTreeMap

__author__ = "{Imad Dabbura}"


class RedBlackTreeMap(BinarySearchTreeMap):
    """Sorted map using implementation of red-black tree."""

    class _Node(BinarySearchTreeMap._Node):
        def __init__(self, parent, left, right, item):
            super().__init__(parent, left, right, item)
            self._red = (
                True
            )  # all new nodes will be red nodes before rebalancing

    def _set_red(self, node):
        node._red = True

    def _set_black(self, node):
        node._red = False

    def _set_color(self, node, make_red):
        node._red = make_red

    def _is_red(self, node):
        return node is not None and node._red

    def _is_red_leaf(self, node):
        return self._is_red(node) and self.is_leaf(node)

    def _get_red_child(self, node):
        for child in self.children(node):
            if self._is_red(child):
                return child
        return None

    def _rebalance_insert(self, node):
        if node == self.root():  # root should be black
            self._set_black(node)
        else:
            parent = self.parent(node)
            # check if there is double-red violation
            if self._is_red(parent):
                uncle = self.sibling(parent)
                if self._is_red(uncle):
                    grand_parent = self.parent(parent)
                    self._set_black(parent)
                    self._set_black(uncle)
                    self._set_red(grand_parent)
                    # keep going up until no double-red violation or reach the root (O(logn))
                    self._rebalance_insert(grand_parent)
                else:
                    # It only happens once; if needed, in any insertion (O(1))
                    middle = self._restructure(node)
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                    self._set_black(middle)

    def _rebalance_delete(self, node):
        if len(self):
            self._set_black(self.root())
        elif node:
            n = self.num_children(node)
            if n == 1:
                child = next(self.children(node))

                # deleted node was black with no children
                if not self._is_red_leaf(child):
                    self._fix_black_deficit(node, child)

            # deleted node was black and has red child (promoted)
            elif n == 2:
                if self._is_red(self.left(node)):
                    self._set_black(self.left(node))
                else:
                    self._set_black(self.right(node))

    def _fix_black_deficit(self, z, y):
        if not self._is_red(y):
            # case 1: y node is black and has one red child
            x = self._get_red_child(y)
            if x:
                old_color = self._is_red(z)
                middle = self._restructure(x)
                self._set_color(middle, old_color)
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))

            # case 2: y node is black and has 2 black children (or None)
            else:
                self._set_red(y)
                if self._is_red(z):
                    self._set_black(z)
                elif not self.is_root(z):
                    self._fix_black_deficit(self.parent(z), self.sibling(z))
        # case 3: y node is red
        else:
            # rotate
            self._rotate(y)
            # recolor
            self._set_black(y)
            self._set_red(z)
            # re-apply algorithm on z's child
            if z == self.left(y):
                self._fix_black_deficit(z, self.right(z))
            else:
                self._fix_black_deficit(z, self.left(z))

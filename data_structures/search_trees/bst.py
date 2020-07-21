from collections.abc import MutableMapping


class BinarySearchTreeMap(MutableMapping):
    class _Item:
        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key < other._key

        def __ne__(self, other):
            return not (self == other)

    class _Node:
        __slots__ = "_parent", "_left", "_right", "_item"

        def __init__(self, parent, left, right, item):
            self._parent = parent
            self._left = left
            self._right = right
            self._item = item

        def key(self):
            return self._item._key

        def value(self):
            return self._item._value

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def is_root(self, node):
        return self.root() is node

    def is_leaf(self, node):
        return self.num_children(node) == 0

    def root(self):
        return self._root

    def parent(self, node):
        return node._parent

    def left(self, node):
        return node._left

    def right(self, node):
        return node._right

    def num_children(self, node):
        count = 0
        if self.left(node):
            count += 1
        if self.right(node):
            count += 1
        return count

    def children(self, node):
        if self.left(node):
            yield self.left(node)
        if self.right(node):
            yield self.right(node)

    def sibling(self, node):
        parent = self.parent(node)
        if parent:
            if node is self.left(parent):
                return self.right(parent)
            return self.left(parent)
        return None

    def _add_root(self, k, v):
        if self.root():
            raise ValueError("Root exists")
        self._root = self._Node(None, None, None, self._Item(k, v))
        self._size += 1
        return self._root

    def _add_left(self, node, k, v):
        if self.left(node):
            raise ValueError("Left child exists")
        node._left = self._Node(node, None, None, self._Item(k, v))
        self._size += 1
        return node._left

    def _add_right(self, node, k, v):
        if self.right(node):
            raise ValueError("Right child exists")
        node._right = self._Node(node, None, None, self._Item(k, v))
        self._size += 1
        return node._right

    def _replace(self, node, k, v):
        old_key = node._item._key
        old_value = node._item._value
        node._item._key = k
        node._item._value = v
        return old_key, old_value

    def _delete(self, node):
        if self.num_children(node) == 2:
            raise ValueError("node has two children")
        child = self.left(node) if self.left(node) else self.right(node)
        if child:
            child._parent = node._parent
        if node is self.root():
            self._root = child
        else:
            parent = node._parent
            if self.left(parent) == node:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        k, v = node.key(), node.value()
        node._item = node._parent = node._left = node._right = None
        return k, v

    def _subtree_search(self, node, k):
        if k == node.key():
            return node
        elif k < node.key() and self.left(node):
            return self._subtree_search(self.left(node), k)
        elif k > node.key() and self.right(node):
            return self._subtree_search(self.right(node), k)
        return node

    def _subtree_search_first(self, node):
        current_node = node
        while self.left(current_node):
            current_node = self.left(current_node)
        return current_node

    def _subtree_search_last(self, node):
        current_node = node
        while self.right(current_node):
            current_node = self.right(current_node)
        return current_node

    def first(self):
        if self.is_empty():
            raise ValueError("Tree is empty")
        return self._subtree_search_first(self.root())

    def last(self):
        if self.is_empty():
            raise ValueError("Tree is empty")
        return self._subtree_search_last(self.root())

    def before(self, node):
        if node:
            if self.left(node):
                return self._subtree_search_last(self.left(node))
            else:
                current_node = node
                parent = self.parent(current_node)
                while parent and current_node == self.left(parent):
                    current_node = parent
                    parent = self.parent(current_node)
                return parent

    def after(self, node):
        if node:
            if self.right(node):
                return self._subtree_search_first(self.right(node))
            else:
                current_node = node
                parent = self.parent(current_node)
                while parent and current_node == self.right(parent):
                    current_node = parent
                    parent = self.parent(current_node)
                return parent

    def find_node(self, k):
        if self.is_empty():
            return None
        node = self._subtree_search(self.root(), k)
        self._rebalance_access(node)
        return node

    def find_min(self):
        if self.is_empty():
            return None
        node = self.first()
        return node.key(), node.value()

    def find_max(self):
        if self.is_empty():
            return None
        node = self.last()
        return node.key(), node.value()

    def find_ge(self, k):
        if self.is_empty():
            return None
        node = self._subtree_search(self.root(), k)
        if node.key() == k:
            return node.key(), node.value()
        else:
            node = self.after(node)
            if node:
                return node.key(), node.value()
            return None

    def find_range(self, start=None, stop=None):
        if not self.is_empty():
            if start is None:
                current_node = self.first()
            else:
                current_node = self.find_node(start)
                if current_node.key() < start:
                    current_node = self.after(start)
            while current_node and (not stop or current_node.key() < stop):
                yield current_node.key(), current_node.value()
                current_node = self.after(current_node)

    def __getitem__(self, k):
        if self.is_empty():
            raise KeyError(f"KeyError: '{k}'")
        node = self._subtree_search(self.root(), k)
        self._rebalance_access(node)
        if not node.key() == k:
            raise KeyError(f"KeyError: '{k}'")
        return node.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            node = self._add_root(k, v)
        else:
            node = self._subtree_search(self.root(), k)
            if node.key() == k:
                node._item._value = v
                self._rebalance_access(node)
                return
            elif node.key() < k:
                self._add_right(node, k, v)
            else:
                self._add_left(node, k, v)
        self._rebalance_insert(node)

    def delete(self, node):
        if self.num_children(node) == 2:
            replacement_node = self.before(node)
            self._replace(
                node, replacement_node.key(), replacement_node.value()
            )
            node = replacement_node
        parent = self.parent(node)
        self._delete(node)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        if not self.is_empty():
            node = self._subtree_search(self.root(), k)
            if node.key() == k:
                self.delete(node)
                return
            self._rebalance_access(node)
        raise KeyError(f"KeyError: '{k}'")

    def _inorder_traversal(self, node):
        if self.left(node):
            for other in self._inorder_traversal(self.left(node)):
                yield other
        yield node
        if self.right(node):
            for other in self._inorder_traversal(self.right(node)):
                yield other

    def __iter__(self):
        if not self.is_empty():
            for node in self._inorder_traversal(self.root()):
                yield node.key()

    def _is_subtree_binary(self, node, min_val, max_val):
        if not node:
            return True
        elif (
            node.key() > min_val
            and node.key() < max_val
            and self._is_subtree_binary(self.left(node), min_val, node.key())
            and self._is_subtree_binary(self.right(node), node.key(), max_val)
        ):
            return True
        return False

    def is_binary(self):
        """Check whether `self` is a binary search tree (BST)."""
        return self._is_subtree_binary(self.root(), float("-inf"), float("inf"))

    def _rebalance_insert(self, node):
        pass

    def _rebalance_delete(self, node):
        pass

    def _rebalance_access(self, node):
        pass

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node."""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child:
            child._parent = parent

    def _rotate(self, node):
        """Rotate node above its parent."""
        x = node
        y = self.parent(x)
        z = self.parent(y)
        if not z:
            self._root = x
            x._parent = None
        else:
            self._relink(z, x, y == self.left(z))
        if x == self.left(y):
            self._relink(y, self.right(x), True)
            self._relink(x, y, False)
        else:
            self._relink(y, self.left(x), False)
            self._relink(x, y, True)

    def _restructure(self, x):
        """Perform trinode restructure of node with its parent/grandparent."""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.left(y)) == (y == self.left(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x

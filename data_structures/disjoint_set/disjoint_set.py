class Partition:
    """Union-find data structure for maintaining disjoint set."""

    class Position:
        __slots__ = ("_size", "_element", "_parent", "_container")

        def __init__(self, e, container):
            self._element = e
            self._parent = (
                self
            )  # at the beginning, each element forms its own group/set
            self._size = 1
            self._container = container

        def element(self):
            return self._element

    def make_group(self, e):
        return self.Position(self, e)

    def find(self, p):
        """Uses path compression heuristic while finding the root."""
        if p._parent != p:
            p._parent = self.find(p._parent)
        return p._parent

    def union(self, p, q):
        """
        Uses union-by-size heuristic to merge two groups/sets if they are not 
        in the same group.
        """
        # get the root of each group
        a = self.find(p)
        b = self.find(q)
        if a != b:
            # make smaller tree the child of longer tree
            if a._size > b._size:
                b._parent = a
                a._size += b._size
            else:
                a._parent = b
                b._size += a._size


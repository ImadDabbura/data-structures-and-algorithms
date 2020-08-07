"""Implementation of Graph using adjacency map ADT."""
from copy import deepcopy


class Graph:
    """Representation of a simple graph using adjacency map."""

    class Vertex:
        __slots__ = "_element"

        def __init__(self, x):
            self._element = x

        def element(self):
            return self._element

        def __hash__(self):
            """This will allow vertex to be a key in set/map."""
            return hash(id(self))

    class Edge:
        __slots__ = ("_origin", "_destination", "_element")

        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def element(self):
            return self._element

        def opposite(self, u):
            return self._origin if u is self._destination else self._destination

        def endpoints(self):
            return (self._origin, self._destination)

        def __hash__(self):
            return hash((self._origin, self._destination))

    def __init__(self, directed=False):
        self._outgoing = {}
        # If the graph is not directed, then incoming is an alias to outgoing
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is self._outgoing

    def insert_vertex(self, x=None):
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}  # in case of directed graph
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
        return e

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(
            len(incident_collection)
            for incident_collection in self._outgoing.values()
        )
        return total if self.is_directed() else total // 2

    def edges(self):
        edges = set(
            (incident_map.values() for incident_map in self._outgoing.values())
        )
        return edges

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def get_edge(self, u, v):
        return self._outgoing.get(u).get(v)

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def remove_vertex(self, v):
        in_adj = self._incoming[v]
        out_adj = self._outgoing[v]
        for u in in_adj:
            del self._outgoing[u][v]
        for u in out_adj:
            del self._incoming[v][u]
        del self._outgoing[v]
        if self.is_directed():
            del self._incoming[v]

    def remove_edge(self, e):
        origin, destination = e.endpoints()
        del self._outgoing[origin][destination]
        del self._incoming[destination][origin]


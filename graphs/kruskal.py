from ..data_structures.priority_queue import HeapPriorityQueue
from ..data_structures.disjoint_set import Partition


def MST_Kruskal(g):
    """
    Compute a minimum spanning tree of a graph using Kruskal's algorithm.
    Return a list of edges that comprise the MST.
    """
    tree = []
    forest = Partition()
    pq = HeapPriorityQueue()
    position = {}

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for edge in g.edges():
        pq.insert(edge.element(), edge)

    size = g.vertex_count()
    while len(tree) < size - 1 and not pq.is_empty():
        _, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a, b)
    return tree

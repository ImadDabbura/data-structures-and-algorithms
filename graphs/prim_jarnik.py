from ..data_structures.priority_queue import AdaptablePriorityQueue


def MST_PrimJarnik(g):
    """
    Compute a minimum spanning tree of a graph using Prim-Jarnik algorithm.
    Return a list of edges that comprise the MST.
    """
    tree = []  # MST
    d = {}  # minimum observed distance to join v with the cloud
    pq = AdaptablePriorityQueue()  # maps d[v] to (v, e(u,v))
    pq_locator = {}

    # set the first vertex's distance to zero (chosen arbitrarly)
    # all other vertices to infinity
    for v in g.vertices():
        if len(d) == 0:
            d[v] = 0
        else:
            d[v] = float("inf")
        # Since no edge exit yet to join any vertex to the cloud
        pq_locator[v] = pq.add(d[v], (v, None))

    while not pq.is_empty():
        _, (u, edge) = pq.remove_min()
        del pq_locator[u]
        if edge is not None:
            tree.append(edge)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            if v in pq_locator:  # if it is not in tree
                w = e.element()
                if w < d[v]:
                    d[v] = w
                    pq.update(pq_locator[v], d[v], (v, e))
    return tree

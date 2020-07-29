from .topological_sort import topological_sort


def shortest_path_dag(g, src):
    """
    Compute shortest-path distances from src to reachable vertices of g.
    Graph g is directed acyclic graph (no cycles).
    1) We first order the vertices using topological_sort order.
    2) Go through the vertices in order from left to right and relax
       all their adjacent vertices.
    """
    d = {}  # d[v] stores distance from src to v
    cloud = {}  # maps all reachable vertices from s to its shortest path

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float("inf")

    topological = topological_sort(g)
    for u in topological:
        for e in g.incident_edges(u, outgoing=True):
            v = e.opposite(u)
            w = e.element()
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                cloud[v] = e
    return cloud

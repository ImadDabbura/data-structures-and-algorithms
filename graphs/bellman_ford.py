def shortest_path_length(g, src):
    """
    Compute shortest-path distances from src to reachable vertices of g.
    Graph g can be undirected or directed, but must be weighted (can be 
    negative) such that e.element() returns a numeric weight for each edge e.
    If there is a negative-weight cycle, there is no unique shortest path.
    Return 1) dictionary mapping each reachable vertex to its distance from src
           2) shortest path tree rooted at vertex src.
           Or  negative cycle.
    """
    d = {}
    cloud = {}
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float("inf")

    size = g.vertex_count()
    for _ in range(size - 1):
        for edge in g.edges():
            u, v = edge.endpoints()
            w = edge.element()
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                cloud[v] = d[v]

    # Check if there is a negative cycle
    for edge in g.edges():
        u, v = edge.endpoints()
        w = edge.element()
        if d[u] + w < d[v]:
            return "There is a negative-weight cycle"

    return cloud

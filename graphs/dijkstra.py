from ..data_structures.priority_queue import AdaptablePriorityQueue


def shortest_path_length(g, src):
    """
    Compute shortest-path distances from src to reachable vertices of g using
    Dijkstra algorithm.
    Graph g can be undirected or directed, but must be weighted (with no 
    negative weights) such that e.element() returns a numeric weight for each 
    edge e.
    Return 1) dictionary mapping each reachable vertex to its distance from src
           2) shortest path tree rooted at vertex src.
    """
    d = {}  # d[v] stores distance from src to v
    cloud = {}  # maps all reachable vertices from s to its shortest path
    tree = {}  # shortest path tree rooted at vertex src
    pq = AdaptablePriorityQueue()  # map d[v] to v
    pq_locator = (
        {}
    )  # map from vertex v to its pq locator so we can use it update

    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float("inf")
        pq_locator[v] = pq.add(d[v], v)

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key
        del pq_locator[u]
        for e in g.incident_edges(u, outgoing=True):
            v = e.opposite(u)
            if v not in cloud:
                w = e.element()
                if d[u] + w < d[v]:
                    d[v] = d[u] + w
                    tree[v] = e
                    pq.update(pq_locator[v], d[v], v)
    return cloud, tree


def shortest_path_tree(g, src, d):
    """
    Reconstruct shortest-path tree rooted at vertex src, given distance map d.
    Return tree as a map from each reachable vertex v (other than src) to the 
    edge e=(u,v) that is used to reach v from its parent u in the tree.
    """
    tree = {}
    for v in d:
        if v is not src:
            for edge in g.incident_edges(u, outgoing=False):
                u = edge.opposite(v)
                w = edge.element()
                if d[u] + w == d[v]:
                    tree[v] = edge
    return tree

def topological_sort(g):
    """
    Returns a list of vertices in directed acyclic graph g in topological 
    order.
    """
    ready = []
    topo = []
    in_count = {}

    for v in g.vertices():
        in_count[v] = g.degree(v, outgoing=False)
        if in_count[v] == 0:  # v has no constraints, i.e no incoming edges
            ready.append(v)

    while len(ready) > 0:
        u = ready.pop()
        topo.append(u)
        for e in g.incident_edges(u):
            v = e.opposite(u)
            in_count[v] -= 1  # v now no longer has u as a constraint
            if in_count[v] == 0:
                ready.append(v)
    return topo

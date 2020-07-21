def BFS(g, u, discovered, component=0, outgoing=True):
    """
    Perform Breadth-First-Search on undiscovered portion of graph g starting at 
    vertex u.
    >>> resutlt = {u: (None, 0)}
    >>> DFS(g, u, resutlt)
    """
    level = [u]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = (e, component)
                    next_level.append(v)
        level = next_level

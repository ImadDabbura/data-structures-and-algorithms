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
            for e in g.incident_edges(u, outgoing):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = (e, component)
                    next_level.append(v)
        level = next_level


def BFS_complete(g, outgoing=True):
    """
    Perform BFS for the entire graph. In the case where the graph is not
    connected, we can count the number of vertces in the forest dictionary 
    that has None value.
    """
    forest = {}
    component = -1
    for v in g.vertices():
        if v not in forest:
            component += 1
            forest[v] = (None, component)
            BFS(g, v, forest, component, outgoing)
    return forest

def DFS(g, u, discovered, component=0, outgoing=True):
    """
    Perform Depth-First-Search on undiscovered portion of graph g starting at 
    vertex u.
    >>> resutlt = {u: (None, 0)}
    >>> DFS(g, u, resutlt)
    """
    for edge in g.incident_edges(u, outgoing):
        v = edge.opposite(u)
        if v not in discovered:
            discovered[v] = (edge, component)
            DFS(g, v, discovered, component, outgoing)


def construct_path(u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            edge, _ = discovered[walk]
            parent = edge.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()
    return path


def DFS_complete(g, outgoing=True):
    """
    Perform DFS for the entire graph. In the case where the graph is not
    connected, we can count the number of vertces in the forest dictionary 
    that has None value.
    """
    forest = {}
    component = -1
    for v in g.vertices():
        if v not in forest:
            component += 1
            forest[v] = (None, component)
            DFS(g, v, forest, component, outgoing)
    return forest


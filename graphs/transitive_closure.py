from copy import deepcopy


def floyd_warshall(g):
    """Returns a new graph that is the transitive closure of g."""
    closure = deepcopy(g)
    vertices = list(closure.vertices())
    n = len(vertices)
    for i in range(n):
        for k in range(n):
            if i != k and g.get_edge(vertices[i], vertices[k]):
                for j in range(n):
                    if i != j != k and g.get_edge(vertices[k], vertices[j]):
                        if not closure.get_edge(vertices[i], vertices[j]):
                            closure.insert_edge(vertices[i], vertices[j])

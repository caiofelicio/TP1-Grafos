def bellman_ford(graph, src) -> tuple:
    dist = [float('inf') for _ in range(len(graph))]
    pred = [None for _ in range(len(graph))]

    dist[src] = 0
    for _ in range(len(graph)):
        changed = False
        for u, v, w, in graph:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u
                changed = True

        if not changed:
            break

    return dist, pred

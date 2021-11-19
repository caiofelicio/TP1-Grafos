def dijkstra(graph, src):
    dist = [float('inf') for _ in range(len(graph))]
    pred = [None for _ in range(len(graph))]

    dist[src] = 0
    q = [i for i in range(len(graph))]

    while q:
        minimum = dist[q[0]]
        u = None
        for i in q:
            if dist[i] <= minimum:
                u = i
                minimum = dist[i]

        q.remove(u)

        for j in graph[u]:
            v, w = j[0], j[1]

            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                pred[v] = u

    return dist, pred

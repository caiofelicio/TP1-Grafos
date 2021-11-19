def floyd_warshall(G) -> tuple:
    V = len(G)  # obtem o numero de vertices do grafo
    dist = [[float('inf') for _ in range(V)] for _ in range(V)]  # inicia a matriz de distancias
    pred = [[None for _ in range(V)] for _ in range(V)]  # inicia a matriz de predecessores

    for i in range(V):
        for j in range(V):
            if i == j:
                dist[i][j] = 0
            elif G[i][j] != 0:
                dist[i][j] = G[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = float('inf')
                pred[i][j] = None

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]

    return dist, pred

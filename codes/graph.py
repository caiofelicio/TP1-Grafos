class Graph:
    def __init__(self, V):
        # inicializa um grafo com V vertices
        self.graph = [[] for _ in range(V)]

    def add_edge(self, u, v, w) -> None:  # metodo para adicionar arestas
        self.graph[u].append([v, w])

    def get_graph(self) -> list:  # retorna o grafo
        return self.graph

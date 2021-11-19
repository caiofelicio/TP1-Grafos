import os
import sys
from datetime import datetime
from codes.dijkstra import dijkstra
from codes.bellman_ford import bellman_ford
from codes.floyd_warshall import floyd_warshall
from codes.find_shortest_path import find_path_between

# define comando para limpar a tela
CLEAN_COMMAND = "cls" if sys.platform == "win32" else "clear"

# definindo cores
RED = "\033[1;31m{}\033[m"
GREEN = "\033[0;32m{}\033[m"
BLUE = "\033[1;34m{}\033[0m"
MAGENTA = "\033[1;35m{}\033[m"
CYAN = "\033[1;36m{}\033[m"
RESET = "\033[0;0m{}\033[m"
BOLD = "\033[;1m{}\033[m"
REVERSE = "\033[;7m{}\033[m"

# definindo os algoritmos que serão usados para
ALGORITHM_LIST = ["Dijkstra", "Bellman Ford", "Floyd Warshall"]
FILES = os.listdir("data")


def menu() -> tuple:
    option, selected_file = None, None

    print(RED.format("=" * 100))
    print(GREEN.format("TEORIA DOS GRAFOS - CSI466".center(100)))
    print("Implementação de Algoritmos para o problema do caminho mínimo em grafos\n".center(100).title())
    print(BLUE.format("Caio Felício de Souza - 19.2.8171".center(100)))
    print(BLUE.format("Gustavo Marques de Mello - 19.2.8048".center(100)))
    print(RED.format("=" * 100) + "\n")

    while True:
        [print(f"{i + 1}) {ALGORITHM_LIST[i]}", end=" " * 10) for i in
         range(len(ALGORITHM_LIST))]  # imprime os algoritmos disponíveis
        try:  # verifica se o usuário digitou um número válido
            option = int(input(
                BLUE.format(
                    "\n\nSelecione o algoritmo para a realização dos testes: ")))  # pede ao usuário para escolher um algoritmo
        except (ValueError, TypeError):  # caso o usuário digite algo diferente de um número
            clean()
            print(RED.format("OPÇÃO INVÁLIDA...\n"))
        else:
            if 1 > option or option > len(
                    ALGORITHM_LIST):  # verifica se o número digitado está dentro do intervalo de 1 ao número de algoritmos
                clean()
                print(RED.format("OPÇÃO INVÁLIDA...\n"))
                continue
            break

    print(BLUE.format(
        f"\nAlgoritmo de {ALGORITHM_LIST[option - 1]} selecionado."))
    print(BLUE.format("Escolha um dos seguinte arquivos para executar os testes:\n"))

    while True:
        [print(f"{i + 1}) {FILES[i]}", end=" " * 5) for i in
         range(len(FILES))]  # imprime os arquivos disponíveis
        try:  # verifica se o usuário digitou um número válido
            selected_file = int(
                input(BLUE.format("\n\nSelecione um dos arquivos acima: ")))  # pede ao usuário para escolher um arquivo
        except (ValueError, TypeError):  # caso o usuário digite algo diferente de um número
            print(RED.format("OPÇÃO INVÁLIDA...\n"))
            continue
        else:
            if selected_file < 1 or selected_file > len(
                    FILES):  # verifica se o número digitado está dentro do intervalo de 1 ao número de arquivos
                print(RED.format("OPÇÃO INVÁLIDA...\n"))
                continue

        return option, "data/" + FILES[
            selected_file - 1]  # retorna o número do algoritmo escolhido e o nome do arquivo escolhido


def run_selected_algorithm(algorithm, G) -> tuple:
    graph = G.get_graph()  # obtem o grafo
    V = len(graph)  # obtem o numero de vertices

    while True:
        print(
            f"\nO grafo selecionado possui {V} vertices, indo de 0 a {V - 1}.")
        start = input("Selecione o vertice de origem: ")
        end = input("Selecione o vertice de destino: ")

        try:
            start, end = int(start), int(end)  # converte para inteiro
        except (ValueError, TypeError):
            clean()
            print(RED.format("OPÇÃO INVÁLIDA...\n"))
            continue
        else:

            if start == end:  # verifica se o vertice de origem é igual ao de destino
                clean()
                print(RED.format(
                    "Os vertices de origem e destino não podem ser iguais.\n"))
                continue

            # verifica se os vertices de origem e destino estão
            # dentro do intervalo [0, V-1]
            if start < 0 or start > V - 1 or end < 0 or end > V - 1:
                clean()
                print(RED.format(
                    "Os vertices de origem e destino devem estar dentro do intervalo [0, V-1].\n"))
                continue
            break

    if algorithm == 1:  # algoritmo de Dijkstra
        start_time = datetime.now()
        dist, pred = dijkstra(graph, start)  # executa o algoritmo de Dijkstra
        # encontra o caminho mais curto entre dois vértices
        min_path = find_path_between(start, end, pred)
        # obtem o tempo de execucao do algoritmo
        end_time = (datetime.now() - start_time).total_seconds()
        cost = dist[end]  # obtem o custo do caminho mais curto
        return start, end, min_path, cost, end_time

    elif algorithm == 2:  # algoritmo de Bellman-Ford
        converted_graph = []  # variavel para armazenar o grafo convertido
        for u in range(len(graph)):
            for v, w in graph[u]:
                converted_graph.append((u, v, w))

        start_time = datetime.now()
        # executa o algoritmo de Bellman-Ford
        dist, pred = bellman_ford(converted_graph, start)
        # encontra o caminho mais curto entre dois vértices
        min_path = find_path_between(start, end, pred)
        # obtem o tempo de execucao do algoritmo
        end_time = (datetime.now() - start_time).total_seconds()
        cost = dist[end]  # obtem o custo do caminho mais curto
        return start, end, min_path, cost, end_time

    else:  # algoritmo de Floyd-Warshall
        # converte o grafo de lista para matriz
        adjacency_matrix = convert_list_to_matrix(graph)
        start_time = datetime.now()
        # executa o algoritmo de Floyd-Warshall
        dist, pred = floyd_warshall(adjacency_matrix)
        # encontra o caminho mais curto entre dois vértices
        min_path = find_path_between(start, end, pred[start])
        # obtem o tempo de execucao do algoritmo
        end_time = (datetime.now() - start_time).total_seconds()
        cost = dist[start][end]  # obtem o custo do caminho mais curto
        return start, end, min_path, cost, end_time


def convert_list_to_matrix(adjacency_list=list) -> list:
    V = len(adjacency_list)
    matrix = [[0 for _ in range(V)] for _ in range(V)]

    for i in range(V):
        for j, w in adjacency_list[i]:
            matrix[i][j] = w  # adiciona o peso da aresta
    return matrix


def clean() -> None:
    os.system(CLEAN_COMMAND)

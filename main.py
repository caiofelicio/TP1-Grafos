from codes.graph import Graph
from utils.utils import menu, run_selected_algorithm, clean, BLUE, RED


def run() -> None:
    algorithm, selected_file = menu()  # obtem o algoritmo e o arquivo de entrada
    with open(selected_file, "r") as file:  # abre o arquivo selecionado para a leitura
        # efetua a leitura da linhas do arquivo e atribui a variabel file_lines
        file_lines = file.readlines()

    # obtem o numero de vertices e arestas que estão na primeira linha do arquivo
    V, E = file_lines[0].split()
    V, E = int(V), int(E)  # convertendo para inteiro

    G = Graph(V)  # cria grafo com V vertices

    for i in range(1, E + 1):  # para cada aresta em E
        u, v, w = file_lines[i].split()  # obtem os vertices e o peso da aresta
        u, v, w = int(u), int(v), int(w)  # converte para inteiro
        G.add_edge(u, v, w)  # adiciona aresta no grafo

    try:
        start, end, min_path, cost, time = run_selected_algorithm(
            algorithm, G)  # executa o algoritmo escolhido
    except TypeError as error:
        print(RED.format("Não existe um caminho entre os vértices selecionados."))
    else:
        print(
            f"\nO caminho minimo entre {RED.format(start)} e {RED.format(end)} é: " + BLUE.format(min_path))
        print("O custo do caminho é: " + BLUE.format(cost))
        print(f"Tempo: {time} segundo(s)")


if __name__ == "__main__":
    while True:
        try:
            clean()
            run()
        except KeyboardInterrupt:
            print("\nPrograma finalizado pelo usuário.")
            exit(1)
        else:
            try:
                run_again = int(
                    input("\nDeseja executar novamente? (1 - Sim, 2 - Não): "))
            except ValueError:
                exit(1)
            else:
                if run_again == 1:
                    continue
                else:
                    break

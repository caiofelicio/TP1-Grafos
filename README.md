# Trabalho 1 - Teoria dos Grafos

## Descrição:
O trabalho consiste em implementar algoritmos para o problema do caminho mínimo em grafos. Os algoritmos a serem desenvolvidos são: _**Dijkstra, Bellman-Ford e Floyd-Warshall.**_

O seu programa deve solicitar ao usuário o nome do arquivo contendo o grafo (no formato **Dimacs**), o algoritmo a ser executado e os vértices de origem e de destino s e t. Como
saída, seu programa deve informar a sequência de vértices do caminho mínimo de s a t, bem como o custo do caminho e o tempo de execução (em segundos) do algoritmo.

## Exemplo:
  ```
  Informe o arquivo : <toy.txt>

  Algoritmo:
      1 Dijkstra
      2 Bellman-Ford
      3 Floyd-Warshall
  <1>

  Origem: <0>
  Destino: <3>
  Processando...
  Caminho: [0, 1, 2, 3]
  Custo: 5
  Tempo: 0.003s
  ```
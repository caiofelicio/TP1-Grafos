def find_path_between(start, end, pred=list) -> list:
    shortest_path = [end]
    aux = end
    while aux != start:
        aux = pred[aux]
        shortest_path.insert(0, aux)

    return shortest_path

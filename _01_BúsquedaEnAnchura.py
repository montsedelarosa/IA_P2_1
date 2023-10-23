# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

from collections import deque

def bfs(graph, start, goal):
    # Inicializamos las estructuras de datos para llevar un seguimiento de los nodos visitados y el camino.
    visited = set()
    queue = deque()
    queue.append([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path  # Si encontramos el objetivo, devolvemos el camino.

        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)

    return None  # Si no se encuentra un camino, devolvemos None.

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo de ejemplo.
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E', 'G'],
        'G': ['F']
    }

    start_node = 'A'
    goal_node = 'G'

    path = bfs(graph, start_node, goal_node)

    if path:
        print(f"Camino de {start_node} a {goal_node}: {path}")
    else:
        print(f"No se encontró un camino de {start_node} a {goal_node}.")

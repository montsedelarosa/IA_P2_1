# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

def iddfs(graph, start, goal):
    depth = 0
    while True:
        result = dls(graph, start, goal, depth)
        if result is not None:
            return result
        depth += 1

def dls(graph, node, goal, depth):
    return recursive_dls(graph, node, goal, depth, [node])

def recursive_dls(graph, node, goal, depth, path):
    if depth == 0 and node != goal:
        return None

    if node == goal:
        return path  # Si encontramos el objetivo, devolvemos el camino.

    if depth > 0:
        for neighbor in graph.get(node, []):
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                result = recursive_dls(graph, neighbor, goal, depth - 1, new_path)
                if result:
                    return result

    return None

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo de ejemplo
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

    path = iddfs(graph, start_node, goal_node)

    if path:
        print(f"Camino de {start_node} a {goal_node}: {path}")
    else:
        print(f"No se encontró un camino de {start_node} a {goal_node}.")

# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

def dfs(graph, node, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(node)
    path = path + [node]

    if node == goal:
        return path

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path)
            if new_path:
                return new_path

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

    path = dfs(graph, start_node, goal_node)

    if path:
        print(f"Camino de {start_node} a {goal_node}: {path}")
    else:
        print(f"No se encontró un camino de {start_node} a {goal_node}.")

# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

def bidirectional_search(graph, start, goal):
    # Inicializamos las estructuras de datos para las búsquedas desde ambos extremos.
    start_queue = [start]
    goal_queue = [goal]
    start_visited = set()
    goal_visited = set()

    while start_queue and goal_queue:
        # Realizamos la búsqueda desde el nodo de inicio.
        current_start = start_queue.pop(0)
        start_visited.add(current_start)

        # Verificamos si el nodo de inicio se encuentra en la búsqueda desde el objetivo.
        if current_start in goal_visited:
            return reconstruct_bidirectional_path(start, goal, current_start)

        for neighbor in graph.get(current_start, []):
            if neighbor not in start_visited:
                start_queue.append(neighbor)

        # Realizamos la búsqueda desde el nodo objetivo.
        current_goal = goal_queue.pop(0)
        goal_visited.add(current_goal)

        # Verificamos si el nodo objetivo se encuentra en la búsqueda desde el inicio.
        if current_goal in start_visited:
            return reconstruct_bidirectional_path(start, goal, current_goal)

        for neighbor in graph.get(current_goal, []):
            if neighbor not in goal_visited:
                goal_queue.append(neighbor)

    return None

def reconstruct_bidirectional_path(start, goal, meeting_node):
    path_start = []
    node = meeting_node
    while node != start:
        path_start.append(node)
        node = meeting_node[0] if meeting_node[0] in graph[node] else meeting_node[1]
    path_start.append(start)
    
    path_goal = []
    node = meeting_node
    while node != goal:
        path_goal.append(node)
        node = meeting_node[0] if meeting_node[0] in graph[node] else meeting_node[1]
    path_goal.append(goal)
    
    path_goal.reverse()
    return path_start + path_goal

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

    path = bidirectional_search(graph, start_node, goal_node)

    if path:
        print(f"Camino de {start_node} a {goal_node}: {path}")
    else:
        print(f"No se encontró un camino de {start_node} a {goal_node}.")

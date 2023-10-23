# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

import heapq

def ucs(graph, start, goal):
    # Inicializamos la cola de prioridad con el nodo de inicio y un costo de cero.
    priority_queue = [(0, start)]
    # Inicializamos un diccionario para llevar un seguimiento de los costos acumulados.
    cost_so_far = {start: 0}
    
    while priority_queue:
        # Extraemos el nodo con el costo acumulado más bajo.
        current_cost, current_node = heapq.heappop(priority_queue)
        
        # Si encontramos el objetivo, reconstruimos el camino y lo devolvemos.
        if current_node == goal:
            return reconstruct_path(start, goal, cost_so_far)
        
        # Exploramos los nodos vecinos.
        for neighbor, cost in graph[current_node]:
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(priority_queue, (new_cost, neighbor))
    
    return None  # Si no se encuentra un camino, devolvemos None.

def reconstruct_path(start, goal, cost_so_far):
    path = [goal]
    while path[-1] != start:
        for neighbor, _ in graph[path[-1]]:
            if cost_so_far[neighbor] + graph[neighbor][path[-1]] == cost_so_far[path[-1]]:
                path.append(neighbor)
                break
    path.reverse()
    return path

# Ejemplo de uso
if __name__ == "__main__":
    # Definimos un grafo de ejemplo donde cada arista tiene un costo.
    graph = {
        'A': [('B', 1), ('C', 3)],
        'B': [('A', 1), ('D', 2), ('E', 4)],
        'C': [('A', 3), ('F', 2)],
        'D': [('B', 2)],
        'E': [('B', 4), ('F', 1)],
        'F': [('C', 2), ('E', 1), ('G', 3)],
        'G': [('F', 3)]
    }
    
    start_node = 'A'
    goal_node = 'G'
    
    path = ucs(graph, start_node, goal_node)
    
    if path:
        print(f"Camino de {start_node} a {goal_node}: {path}")
    else:
        print(f"No se encontró un camino de {start_node} a {goal_node}.")

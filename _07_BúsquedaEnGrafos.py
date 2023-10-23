# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

    def bfs(self, start_node, goal_node):
        visited = set()
        queue = [start_node]
        while queue:
            node = queue.pop(0)
            if node == goal_node:
                return True
            if node not in visited:
                visited.add(node)
                queue.extend(self.graph.get(node, []))
        return False

# Ejemplo de uso
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'F')

    start_node = 'A'
    goal_node = 'F'

    if graph.bfs(start_node, goal_node):
        print(f"Existe un camino entre {start_node} y {goal_node}.")
    else:
        print(f"No existe un camino entre {start_node} y {goal_node}.")

from queue import PriorityQueue

def a_star(graph, h, start, goal):
    pq = PriorityQueue()
    pq.put((0, start))
    g = {start: 0}
    parent = {start: None}

    while not pq.empty():
        _, node = pq.get()
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1]

        for neighbor, cost in graph[node]:
            new_cost = g[node] + cost
            if neighbor not in g or new_cost < g[neighbor]:
                g[neighbor] = new_cost
                f = new_cost + h[neighbor]
                pq.put((f, neighbor))
                parent[neighbor] = node

# Graph and heuristic
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [], 'E': [('F', 2)], 'F': []
}
h = {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 1, 'F': 0}
print(a_star(graph, h, 'A', 'F'))

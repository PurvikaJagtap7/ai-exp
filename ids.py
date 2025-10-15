# Iterative Deepening Search (IDS) with path output

def dls(graph, start, goal, limit, path):
    path.append(start)
    if start == goal:
        return path
    if limit <= 0:
        path.pop()
        return None

    for neighbor in graph.get(start, []):
        if neighbor not in path:
            result = dls(graph, neighbor, goal, limit - 1, path)
            if result:
                return result

    path.pop()
    return None


def ids(graph, start, goal, max_depth):
    for depth in range(max_depth + 1):
        print(f"Searching at depth: {depth}")
        path = []
        result = dls(graph, start, goal, depth, path)
        if result:
            return result
    return None


# Example graph (Adjacency List)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'
max_depth = 5

result = ids(graph, start_node, goal_node, max_depth)

if result:
    print("\nGoal found!")
    print("Path to goal:", " → ".join(result))
else:
    print("\nGoal not found within given depth.")

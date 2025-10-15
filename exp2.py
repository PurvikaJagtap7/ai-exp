from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, start, goal):
        visited = set()
        stack = [(start, [start])]
        
        print("DFS Traversal:")
        
        while stack:
            current, path = stack.pop()
            
            if current not in visited:
                visited.add(current)
                print(f"Visiting: {current}, Stack: {[item[0] for item in stack]}")
                
                if current == goal:
                    print(f"Goal '{goal}' found!")
                    print(f"Path: {' -> '.join(path)}")
                    return path
                
                # Add neighbors to stack (reverse order for correct DFS)
                for neighbor in reversed(self.graph[current]):
                    if neighbor not in visited:
                        stack.append((neighbor, path + [neighbor]))
        
        print(f"Goal '{goal}' not found!")
        return None

# Example usage
def dfs_example():
    g = Graph()
    
    # Create a sample graph
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), 
             ('C', 'F'), ('C', 'G'), ('D', 'H'), ('E', 'I')]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    print("Graph structure:")
    for node, neighbors in g.graph.items():
        print(f"{node}: {neighbors}")
    
    print("\n" + "="*40)
    path = g.dfs('A', 'I')
    
    if path:
        print(f"\nPath found: {' -> '.join(path)}")
        print(f"Path length: {len(path) - 1}")

if __name__ == "__main__":
    dfs_example()
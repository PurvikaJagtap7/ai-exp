from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs_limited(self, start, goal, depth_limit, path):
        if depth_limit == 0:
            if start == goal:
                return path + [start]
            else:
                return None
        
        if depth_limit > 0:
            if start == goal:
                return path + [start]
            
            for neighbor in self.graph[start]:
                result = self.dfs_limited(neighbor, goal, depth_limit - 1, path + [start])
                if result:
                    return result
        
        return None
    
    def iterative_deepening_search(self, start, goal, max_depth=10):
        print(f"Starting Iterative Deepening Search from '{start}' to '{goal}'")
        print("="*50)
        
        for depth in range(max_depth + 1):
            print(f"\nDepth limit: {depth}")
            result = self.dfs_limited(start, goal, depth, [])
            
            if result:
                print(f"Goal found at depth {depth}!")
                print(f"Path: {' -> '.join(result)}")
                return result
            else:
                print(f"Goal not found within depth {depth}")
        
        print(f"\nGoal not found within maximum depth {max_depth}")
        return None

# Example usage
def idds_example():
    g = Graph()
    
    # Create a sample tree/graph
    edges = [('S', 'A'), ('S', 'B'), ('A', 'C'), ('A', 'D'), 
             ('B', 'E'), ('B', 'F'), ('C', 'G'), ('D', 'H'), 
             ('E', 'I'), ('F', 'J')]
    
    for u, v in edges:
        g.add_edge(u, v)
    
    print("Graph structure:")
    for node, neighbors in g.graph.items():
        print(f"{node}: {neighbors}")
    
    print("\n" + "="*50)
    path = g.iterative_deepening_search('S', 'J', max_depth=5)

if __name__ == "__main__":
    idds_example()
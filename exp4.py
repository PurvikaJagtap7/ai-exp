import heapq
import math

class Node:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.g = float('inf')  # Cost from start
        self.h = 0  # Heuristic cost to goal
        self.f = float('inf')  # Total cost
        self.parent = None
    
    def __lt__(self, other):
        return self.f < other.f

class AStarGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    
    def add_node(self, name, x, y):
        self.nodes[name] = Node(name, (x, y))
        self.edges[name] = []
    
    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append((to_node, cost))
        self.edges[to_node].append((from_node, cost))  # For undirected graph
    
    def heuristic(self, node1, node2):
        # Euclidean distance
        x1, y1 = self.nodes[node1].position
        x2, y2 = self.nodes[node2].position
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def a_star(self, start, goal):
        open_list = []
        closed_set = set()
        
        # Initialize start node
        start_node = self.nodes[start]
        start_node.g = 0
        start_node.h = self.heuristic(start, goal)
        start_node.f = start_node.g + start_node.h
        
        heapq.heappush(open_list, start_node)
        
        print(f"A* Search from {start} to {goal}")
        print("="*40)
        
        step = 1
        while open_list:
            current = heapq.heappop(open_list)
            current_name = current.name
            
            print(f"Step {step}: Exploring {current_name}")
            print(f"  g({current_name}) = {current.g}")
            print(f"  h({current_name}) = {current.h:.2f}")
            print(f"  f({current_name}) = {current.f:.2f}")
            
            if current_name == goal:
                print(f"\nGoal reached!")
                return self.reconstruct_path(current)
            
            closed_set.add(current_name)
            
            # Explore neighbors
            for neighbor_name, edge_cost in self.edges[current_name]:
                if neighbor_name in closed_set:
                    continue
                
                neighbor = self.nodes[neighbor_name]
                tentative_g = current.g + edge_cost
                
                if tentative_g < neighbor.g:
                    neighbor.parent = current
                    neighbor.g = tentative_g
                    neighbor.h = self.heuristic(neighbor_name, goal)
                    neighbor.f = neighbor.g + neighbor.h
                    
                    if neighbor not in open_list:
                        heapq.heappush(open_list, neighbor)
                        print(f"    Added {neighbor_name} to open list: f = {neighbor.f:.2f}")
            
            step += 1
        
        print("No path found!")
        return None
    
    def reconstruct_path(self, node):
        path = []
        current = node
        total_cost = node.g
        
        while current:
            path.append(current.name)
            current = current.parent
        
        path.reverse()
        print(f"Path: {' -> '.join(path)}")
        print(f"Total cost: {total_cost}")
        return path

# Example usage
def astar_example():
    graph = AStarGraph()
    
    # Add nodes with positions (x, y)
    nodes_data = [
        ('A', 0, 0), ('B', 1, 2), ('C', 3, 1), ('D', 2, 4),
        ('E', 4, 3), ('F', 1, 0), ('G', 2, 1), ('H', 3, 4),
        ('I', 4, 2), ('J', 5, 3)
    ]
    
    for name, x, y in nodes_data:
        graph.add_node(name, x, y)
    
    # Add edges with costs
    edges_data = [
        ('A', 'B', 6), ('A', 'F', 3), ('B', 'D', 3), ('B', 'C', 3),
        ('F', 'G', 1), ('G', 'I', 3), ('C', 'E', 5), ('C', 'I', 4),
        ('I', 'J', 3), ('D', 'H', 2), ('E', 'J', 2)
    ]
    
    for from_node, to_node, cost in edges_data:
        graph.add_edge(from_node, to_node, cost)
    
    path = graph.a_star('A', 'J')

if __name__ == "__main__":
    astar_example()
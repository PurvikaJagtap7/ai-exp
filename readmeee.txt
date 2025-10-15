1️⃣ Depth-First Search (DFS) Algorithm

Goal: Explore paths deeply to find a goal node.

Algorithm (Pointwise):

Start at the Start node and mark it as visited.

If the current node = Goal, return path.

For each neighbor of the current node:

If neighbor is not visited:

Recursively call DFS on the neighbor.

If goal found in recursion, return path.

If all neighbors explored and goal not found, return failure.

2️⃣ Iterative Deepening Search (IDS) Algorithm

Goal: Combine DFS’s space efficiency with BFS’s completeness.

Algorithm (Pointwise):

Initialize depth d = 0.

Repeat until goal found or maximum depth reached:

Call Depth-Limited Search (DLS) with depth limit d.

If DLS returns a path, stop and return path.

Otherwise, increment d = d + 1.

If maximum depth reached and goal not found, return failure.

Depth-Limited Search (DLS) Step:

Start at node, keep track of depth.

If node = goal → return path.

If depth limit reached → return failure.

Recursively explore neighbors not visited.

3️⃣ Minimax Algorithm

Goal: In a 2-player game, choose the optimal move assuming the opponent plays optimally.

Algorithm (Pointwise):

Start at the current game state (root node).

If node is a terminal state (win/loss/draw) or max depth reached:

Return evaluation score of node.

If it’s Max player’s turn:

Initialize best = -∞.

For each child node (possible move):

Call Minimax recursively on child.

Update best = max(best, child value).

Return best.

If it’s Min player’s turn:

Initialize best = +∞.

For each child node:

Call Minimax recursively on child.

Update best = min(best, child value).

Return best.

Repeat until the root chooses the best move.

4️⃣ A* (A-Star) Search Algorithm

Goal: Find the shortest path from Start → Goal using cost + heuristic.

Algorithm (Pointwise):

Initialize open list with the start node.

Initialize closed list as empty.

While open list is not empty:

Select node n with lowest f(n) = g(n) + h(n) from open list.

g(n) = cost from start to n

h(n) = heuristic estimate from n to goal

If n = Goal, return path.

Move n to closed list.

For each neighbor of n:

If neighbor is in closed list → skip.

Calculate g(neighbor) and f(neighbor).

If neighbor not in open list or has lower f-value → add/update it in open list.

If open list empty and goal not found → return failure.
# Graphs Pattern

**Author:** Ritesh Rana

## Introduction to Graphs

Graphs are versatile data structures consisting of vertices (nodes) connected by edges. They can represent relationships, networks, paths, and many real-world scenarios. Graph algorithms are fundamental in computer science and appear frequently in coding interviews, covering traversal, shortest paths, connectivity, and optimization problems.

### Key Concepts

**Basic Terminology:**
- **Vertex/Node**: Individual element in the graph
- **Edge**: Connection between two vertices
- **Adjacent**: Two vertices connected by an edge
- **Path**: Sequence of vertices connected by edges
- **Cycle**: Path that starts and ends at the same vertex
- **Connected**: All vertices reachable from each other

**Types of Graphs:**
1. **Directed vs Undirected**: Edges have direction or not
2. **Weighted vs Unweighted**: Edges have associated costs or not
3. **Connected vs Disconnected**: All vertices reachable or not
4. **Cyclic vs Acyclic**: Contains cycles or not (DAG)

### Common Patterns

1. **Graph Traversal** - DFS and BFS exploration
2. **Shortest Path** - Finding minimum cost paths
3. **Cycle Detection** - Identifying cycles in graphs
4. **Topological Sort** - Ordering vertices in DAG
5. **Connected Components** - Finding isolated groups
6. **Bipartite Testing** - Two-coloring problems
7. **Minimum Spanning Tree** - Connecting all vertices with minimum cost

### When to Use Graphs

- Social networks and relationships
- Transportation and routing problems
- Dependencies and prerequisites
- Web crawling and link analysis
- Game states and decision trees
- Network flow problems

### Graph Representation

**Adjacency List:** Most common, space-efficient
```python
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
```

**Adjacency Matrix:** Good for dense graphs
```python
# For n vertices, create n x n matrix
matrix = [[0, 1, 1, 0],
          [1, 0, 0, 1],
          [1, 0, 0, 1],
          [0, 1, 1, 0]]
```

## Problems Covered

1. Introduction to Graphs
2. Graph Deep Copy
3. Count Islands
4. Matrix Infection
5. Bipartite Graph Validation
6. Longest Increasing Path
7. Shortest Transformation Sequence
8. Merging Communities
9. Prerequisites
10. Shortest Path
11. Connect the Dots

## Interview Tips for Graphs

💡 **Key Interview Tips:**

1. **Choose representation** - Adjacency list vs matrix based on problem
2. **Consider direction** - Directed vs undirected affects algorithm
3. **Track visited nodes** - Prevent infinite loops in traversal
4. **Think about edge cases** - Disconnected graphs, self-loops, cycles
5. **Understand time complexity** - V + E for most algorithms

### Implementation Examples

**Depth-First Search (DFS):**
```python
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start)
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    
    return visited
```

**Breadth-First Search (BFS):**
```python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex)
        
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return visited
```

**Detect Cycle in Directed Graph:**
```python
def has_cycle(graph):
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {node: WHITE for node in graph}
    
    def dfs(node):
        if color[node] == GRAY:
            return True  # Back edge found
        
        if color[node] == BLACK:
            return False
        
        color[node] = GRAY
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
        
        color[node] = BLACK
        return False
    
    for node in graph:
        if color[node] == WHITE:
            if dfs(node):
                return True
    
    return False
```

**Shortest Path (Dijkstra's Algorithm):**
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
```

**Count Islands (DFS on Grid):**
```python
def count_islands(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            grid[r][c] == '0'):
            return
        
        grid[r][c] = '0'  # Mark as visited
        
        # Explore all 4 directions
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    
    return count
```

### Common Pitfalls and How to Avoid Them

1. **Infinite Loops**
   - Always track visited nodes
   - Handle cycles properly

2. **Direction Confusion**
   - Be clear about directed vs undirected
   - Add edges in correct direction

3. **Memory Issues**
   - Be careful with deep recursion in DFS
   - Consider iterative approaches for large graphs

---
*Master graph algorithms to solve complex relationship and pathfinding problems!*
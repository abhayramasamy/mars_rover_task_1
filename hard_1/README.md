# Mars Rover Pathfinding: Hard Problem 1

## <span style="color: #FF4500; font-family: Arial, sans-serif;">Problem Description</span>

This project implements a pathfinding solution for a Mars rover navigating a grid-based terrain with obstacles. The rover must find an optimal path from a starting position to a goal position while avoiding obstacles defined by their distances from the origin (0,0) in four directions: north, east, south, and west.

The grid is a square map of size n × n (where n is odd to center the origin), with obstacles represented as blocked cells. The challenge involves reading obstacle data from a file, constructing the grid, and applying search algorithms to find collision-free paths.

## <span style="color: #32CD32; font-family: Arial, sans-serif;">Inputs</span>

1. **Obstacle Data**: Read from `obstacles.txt`, each line contains four integers representing distances from origin: north, east, south, west.
2. **Grid Size**: User input for n (odd integer) defining the n × n grid.
3. **Start Coordinates**: User input as (x, y) tuple in coordinate system.
4. **Goal Coordinates**: User input as (x, y) tuple in coordinate system.

Coordinates are transformed to grid indices (origin at center).

## <span style="color: #1E90FF; font-family: Arial, sans-serif;">What It Does</span>

The program:
- Parses obstacle data and builds a 2D grid representation
- Transforms user coordinates to grid indices
- Implements Breadth-First Search (BFS) and A* algorithms
- Finds paths from start to goal avoiding obstacles
- Converts paths to directional movement instructions

## <span style="color: #FFD700; font-family: Arial, sans-serif;">Output</span>

- Grid visualization with obstacles
- Path found by BFS (list of grid coordinates)
- Path found by A* (list of grid coordinates)
- Movement instructions (e.g., "North 1", "East 1") based of A* results.

## <span style="color: #FF69B4; font-family: Arial, sans-serif;">How It Works</span>

1. Read obstacles from file and build grid (1=free, 0=obstacle)
2. Get user inputs for grid size, start, and goal
3. Transform coordinates to grid indices
4. Run BFS and A* algorithms
5. Reconstruct paths from parent arrays
6. Convert paths to movement commands

## <span style="color: #8A2BE2; font-family: Arial, sans-serif;">Algorithms Implemented</span>

### Breadth-First Search (BFS)
- Explores nodes level by level
- Uses queue (deque) for frontier
- Guarantees shortest path in unweighted graphs

### A* Search
- Informed search using priority queue
- Combines actual cost (g) and heuristic estimate (h)
- Uses Manhattan distance as admissible heuristic

## <span style="color: #DC143C; font-family: Arial, sans-serif;">About the Algorithms</span>

**BFS**: Uninformed search, explores all neighbors at current depth before moving deeper. Optimal for unweighted grids but can be inefficient in large spaces.

**A***: Best-first search guided by f(n) = g(n) + h(n), where g(n) is path cost from start, h(n) is heuristic to goal. Manhattan distance |dx| + |dy| is admissible (never overestimates true cost).

## <span style="color: #00CED1; font-family: Arial, sans-serif;">Why A* Might Be Better Than BFS</span>

A* is more efficient than BFS in grids with obstacles because:
- **Informed Search**: Heuristic guides exploration toward goal
- **Reduced Node Expansion**: Avoids exploring irrelevant areas
- **Optimality**: Finds shortest path with admissible heuristic
- **Performance**: Often explores fewer nodes than BFS in practice

In uniform-cost grids, both find shortest paths, but A* typically does so faster.

## <span style="color: #FF6347; font-family: Arial, sans-serif;">Case Where A* Provides Shorter Path Than BFS</span>

Consider a 5×5 grid with start at (0,0) and goal at (4,4). Obstacles block direct paths, forcing detours.

```
Grid:
S . . # .
. # . . .
. . # . .
. . . # .
. . . . G

# = obstacle, S = start, G = goal
```

BFS explores uniformly, potentially taking a longer route around obstacles. A* with Manhattan heuristic prioritizes moves reducing distance to goal, finding a shorter path by intelligently navigating around obstacles.

In this code's uniform cost, path lengths are same, but A* finds it more efficiently.

## <span style="color: #20B2AA; font-family: Arial, sans-serif;">Learning Experience</span>

Implementing pathfinding algorithms deepened understanding of graph search. BFS reinforced breadth-first principles, while A* showed heuristic power. Grid coordinate transformation and obstacle mapping were key challenges. This project enhanced algorithmic thinking and Python implementation skills.

## <span style="color: #FFA500; font-family: Arial, sans-serif;">Equations, Theorems, and Sketches</span>

### A* Cost Function
$$f(n) = g(n) + h(n)$$

Where:
- $g(n)$: Cost from start to node n
- $h(n)$: Heuristic estimate from n to goal
- $f(n)$: Total estimated cost

### Manhattan Distance Heuristic
$$h(n) = |x_{goal} - x_n| + |y_{goal} - y_n|$$

### Grid Sketch
```
Origin (0,0) at center
North: +x, South: -x
East: +y, West: -y

Grid indices: (row, col)
(0,0) at top-left in array
```

## <span style="color: #9370DB; font-family: Arial, sans-serif;">Challenges Faced</span>

- Coordinate system transformation (world to grid)
- Handling out-of-bounds obstacles
- Implementing parent tracking for path reconstruction
- Ensuring grid size is odd for centered origin
- Debugging path conversion to moves

## <span style="color: #3CB371; font-family: Arial, sans-serif;">Approach</span>

1. Analyze problem: Grid pathfinding with obstacles
2. Design data structures: 2D arrays for grid, parent tracking
3. Implement BFS first for baseline
4. Add A* with Manhattan heuristic
5. Test with various obstacle configurations
6. Add path-to-moves conversion.
   
## library used:
1. Numpy
2. collections
3. heapq

## <span style="color: #FF1493; font-family: Arial, sans-serif;">Resources Used</span>

- Python documentation for heapq, deque, numpy
- Geeks for geeks
- Stack Overflow
- Mars rover simulation concepts from robotics literature</content>
<parameter name="filePath">c:\Users\ABHAY RAMASAMY\Desktop\IITMBSDS\mars_rover\README.md

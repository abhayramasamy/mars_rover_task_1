"""
HARD PROBLEM 1: PATH FINDING IN A GRID WITH OBSTACLES
MaRs club task 1
The lsit of obstaces present in the surroundings are given in a txt file in the form of tupkes showing the 
distances of the obstacles from the origin (0,0) in the north, east, south and west directions.
The task is to find a path from a given start coordinate to a goal coordinate while avoiding the obstacles.
"""
import heapq
import numpy as np
from collections import deque
#import the libraries, numpy-->array heapq-->priority queue, deque-->queue for bfs

#the obstacles are actually read form a txt file
#file name is obstacles.txt has any number of rows but 4 columns representing the north, east, south and west distances of the obstacle from the origin (0,0) which is the center of the grid
with open('obstacles.txt', 'r') as f:
    obstacles_stored = []
    for line in f:
        obs = list(map(int, line.strip().split()))
        obstacles_stored.append(obs)
#obtain the map size from the user, the map is a square grid of size n x n, 
#where n is an odd integer to ensure that the origin (0,0) is at the center of the grid. 

map_size = int(input("Enter the size of the grid (n x n): ")) 
while map_size % 2 == 0:
    print("Please enter an odd integer for the map size to ensure that the origin is at the center of the grid.")
    map_size = int(input("Enter the size of the grid (n x n): "))

#This function build a grid map based on th map size and obstacle listing from the txt file, 
#the grid is represented as a 2D numpy array where 1 represents a free cell and 0 represents an obstacle. 
#The function also returns the coordinates of the origin (0,0) in the grid, which is at the center of the grid.
def build_map(no, obstacles):
    grid = np.ones((no,no), dtype=int)
    (ox, oy) = (no//2, no//2)
    for obs in obstacles:
        n,e,s,w = obs
        dx = n-s
        dy = w-e
        if 0<=(ox+dx)<no and 0<=(oy+dy)<no:
            grid[ox+dx][oy+dy]=0 
        else:
            print("Obstacle at ({}, {}) is out of bounds and will be ignored.".format(ox+dx, oy+dy))
            continue
    return grid, (ox, oy)

print(build_map(map_size, obstacles_stored)) #display the grid map

start = tuple(map(int, input("Enter the start coordinates (x, y): ").split())) #obtain current place
goal = tuple(map(int, input("Enter the goal coordinates (x, y): ").split()))   #destination coordinates


#transform the coordinates to the grid indexing
def transform_coordinates(coord, n):
    x, y = coord
    transformed_x = x + n//2
    transformed_y = y + n//2
    if 0 <= transformed_x < n and 0 <= transformed_y < n:
        return (transformed_x, transformed_y)
    else:
        raise ValueError("Coordinates ({}, {}) are out of bounds for grid size {}. choose an index within the grid. <map_size>".format(x, y, n))
    
start = transform_coordinates(start, map_size)   #transform the start and goal coordinates to the grid indexing
goal = transform_coordinates(goal, map_size)     #, which is necessary for the pathfinding algorithms to work correctly.


#Breadth First Search (BFS) implementation to find the path from start to goal in the grid.
def bfs(grid, start, goal, n):
    parent = [[None for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)] 
    queue = deque([start])  #normal queue for BFS, stores the nodes to be explored
    visited[start[0]][start[1]]=True
    parent[start[0]][start[1]]=None

    while queue:
        curr = queue.popleft()
        if curr==goal:
            break
        for dx, dy in [(-1, 0), (1,0), (0, -1), (0, 1)]: #checks 4 adj cells
            child = (curr[0]+dx, curr[1]+dy)
            if 0<=child[0]<n and 0<=child[1]<n and not visited[child[0]][child[1]] and grid[child[0]][child[1]]==1:
                visited[child[0]][child[1]]=True
                parent[child[0]][child[1]]=curr
                queue.append(child)
    return parent
#BFS returns the parent array which can be used to reconstruct the path from the goal back to the start.
path = []
parent = bfs(build_map(map_size, obstacles_stored)[0], start, goal, map_size)
curr = goal
while curr is not None: 
    path.append(curr)
    curr = parent[curr[0]][curr[1]]      
path.reverse()
print("Path found:", path)


#a* algorithm implemetnation
#A* is a popular pathfinding algorithm that combines the advantages of Dijkstra's algorithm and Greedy Best-First Search.

#We need to minimize the total cost f(n) = g(n) + h(n), where g(n) is the cost from the start node to the current node n,
#and h(n) is the heuristic estimate of the cost from n to the goal.

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
    #manhattan distance

def a_start(grid, start, goal, n):
    n = len(grid)
    g = [[float('inf') for _ in range(n)] for _ in range(n)]
    parent = [[None]*n for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    g[start[0]][start[1]]=0  #cost from start to start is 0
    pq = [] #a priority queue storess nodes with minimal cost being popped first
    heapq.heappush(pq, (heuristic(start, goal), start))    
    while pq:
        _, curr = heapq.heappop(pq)
        if curr==goal:
            break
        if visited[curr[0]][curr[1]]:
            continue
        visited[curr[0]][curr[1]]=True 
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            child = (curr[0]+dx, curr[1]+dy)
            if 0<=child[0]<n and 0<=child[1]<n and grid[child[0]][child[1]] == 1:
                tent_g = g[curr[0]][curr[1]]+1
                if tent_g < g[child[0]][child[1]]:
                    g[child[0]][child[1]] = tent_g
                    parent[child[0]][child[1]]=curr 
                    heapq.heappush(pq, (tent_g + heuristic(child, goal), child))
    return parent, g

parent, g = a_start(build_map(map_size, obstacles_stored)[0], start, goal, map_size)
#build the path from the parent array returned by A* algorithm, similar to BFS
path = []
curr = goal
while curr is not None:
    path.append(curr)
    curr = parent[curr[0]][curr[1]]

path.reverse()
print("Path found by A*:", path)

#Convert the path of coordinates to a list of instructions for the robot to follow
def path_to_moves(path):
    moves = []

    for i in range(len(path) - 1):
        x1, y1 = path[i]
        x2, y2 = path[i + 1]

        dx = x2 - x1
        dy = y2 - y1

        if dx == -1 and dy == 0:
            moves.append("North 1")
        elif dx == 1 and dy == 0:
            moves.append("South 1")
        elif dx == 0 and dy == 1:
            moves.append("East 1")
        elif dx == 0 and dy == -1:
            moves.append("West 1")

    return moves
print("Moves to reach the goal:", path_to_moves(path))



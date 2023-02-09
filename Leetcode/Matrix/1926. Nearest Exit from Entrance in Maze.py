# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') 
# and walls (represented as '+'). You are also given the entrance of the maze, 
# where entrance = [entrancerow, entrancecol] denotes the row and column of the
#  cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into
#  a cell with a wall, and you cannot step outside the maze. Your goal is to find the
#   nearest exit from the entrance. An exit is defined as an empty cell that is at the
#    border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit,
#  or -1 if no such path exists.

# You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') 
# and walls (represented as '+'). You are also given the entrance of the maze,
#  where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

# In one step, you can move one cell up, down, left, or right. You cannot step into a 
# cell with a wall, and you cannot step outside the maze. Your goal is to find the
#  nearest exit from the entrance. An exit is defined as an empty cell that is at the 
#  border of the maze. The entrance does not count as an exit.

# Return the number of steps in the shortest path from the entrance to the nearest exit, 
# or -1 if no such path exists.

# Approach 1: Breadth First Search (BFS)
# Intuition
# This problem is about finding the shortest path in a matrix, thus Breadth First Search (BFS) is a promising method.

# Why BFS over Depth First Search (DFS) for this problem?

# The reason is that DFS is not guaranteed to find the shortest path, as it will explore 
# the matrix as much as possible before moving on to another branch. As shown in the picture
#  below, we may explore the matrix along the green or orange paths first, but these are not the shortest path.

# In BFS, however, we explore cells by the order of their distance from the starting position,
#  so whenever we reach an exit cell, we are guaranteed that it is the closest exit!

# img

# In BFS, we explore cells in the order of their distance from the starting position. 
# We will first visit the cell with a distance of 000, then move on to all the cells with
#  a distance of 111, then move on to all the cells with a distance of 222, and so forth.

# img

# We use a queue as the container to store all the cells to be visited. Since the
#  operation on a queue is done in First In, First Out (FIFO) order, it allows us 
#  to explore all the cells with distance d which we previously stored, before moving 
#  on to cells with larger distance d + 1!

# How do we prevent revisiting the same cells?

# Upon finding an unvisited neighbor cell, we mark it as visited before adding it to the queue, 
# and we skip these visited cells during further searches. Thus, each empty cell will be added to 
# the queue at most once. (Since the input matrix maze use different characters to separate empty 
# cells (.) and walls (+), we can take advantage of this by marking cells to be visited as +.)

# Let's take a look at the following slides as an example:

# Current


# Algorithm
# Initialize an empty queue queue to store all the nodes to be visited.
# Add entrance and its distance 000 to queue and mark entrance as visited.
# While we don't reach an exit and queue still has cells, pop the first cell from queue. 
# Suppose its distance from entrance is curr_distance. We check its neighboring cells in all 
# four directions, if it has an unvisited neighbor cell:
# If this neighbor cell is an exit, return its distance from the starting position,
#  curr_distance + 1, as the nearest distance.
# Otherwise, we mark it as visited, and add it to queue along with its distance curr_distance + 1.
# If we finish the iteration and no exit is found, return -1.


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        
        # Mark the entrance as visited since its not a exit.
        start_row, start_col = entrance
        maze[start_row][start_col] = "+"
        
        # Start BFS from the entrance, and use a queue `queue` to store all 
        # the cells to be visited.
        queue = collections.deque()
        queue.append([start_row, start_col, 0])
        
        while queue:
            curr_row, curr_col, curr_distance = queue.popleft()
            
            # For the current cell, check its four neighbor cells.
            for d in dirs:
                next_row = curr_row + d[0]
                next_col = curr_col + d[1]
                
                # If there exists an unvisited empty neighbor:
                if 0 <= next_row < rows and 0 <= next_col < cols \
                    and maze[next_row][next_col] == ".":
                    
                    # If this empty cell is an exit, return distance + 1.
                    if 0 == next_row or next_row == rows - 1 or 0 == next_col or next_col == cols - 1:
                        return curr_distance + 1
                    
                    # Otherwise, add this cell to 'queue' and mark it as visited.
                    maze[next_row][next_col] = "+"
                    queue.append([next_row, next_col, curr_distance + 1])
            
        # If we finish iterating without finding an exit, return -1.
        return -1

from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS, COLS = len(maze), len(maze[0])
        r,c = entrance
        queue = deque([(r,c,0)])
        visited = set([(r,c)])
        
        while queue:
            r,c,d = queue.popleft()
            
            if d != 0 and (r + 1 == ROWS or r - 1 == -1 or c + 1 == COLS or c - 1 == -1):
                return d
            
            for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                nr,nc = r+dr, c+dc
                
                if ROWS > nr >= 0 <= nc < COLS and maze[nr][nc] != '+' and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    queue.append((nr,nc,d+1))
        
        return -1

# TC -> O(mn)
# SC -> O(max(m,n))
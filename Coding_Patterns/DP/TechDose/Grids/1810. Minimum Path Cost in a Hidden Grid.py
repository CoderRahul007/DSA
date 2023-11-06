# https://leetcode.ca/2021-06-01-1810-Minimum-Path-Cost-in-a-Hidden-Grid/#:~:text=Explanation%3A%20The%20minimum%20cost%20path%20is%20%282%2C0%29,-%3E%20%282%2C1%29%20-%3E%20%281%2C1%29%20-%3E%20%281%2C2%29%20-%3E%20%280%2C2%29.

# There is a robot in a hidden grid, and you are trying to get it from its starting cell to the target cell in this grid. The grid is of size m x n, and each cell in the grid is either empty or blocked. It is guaranteed that the starting cell and the target cell are different, and neither of them is blocked.

# Each cell has a cost that you need to pay each time you move to the cell. The starting cell’s cost is not applied before the robot moves.

# You want to find the minimum total cost to move the robot to the target cell. However, you do not know the grid’s dimensions, the starting cell, nor the target cell. You are only allowed to ask queries to the GridMaster object.

# The GridMaster class has the following functions:

# boolean canMove(char direction) Returns true if the robot can move in that direction. Otherwise, it returns false.
# int move(char direction) Moves the robot in that direction and returns the cost of moving to that cell. If this move would move the robot to a blocked cell or off the grid, the move will be ignored, the robot will remain in the same position, and the function will return -1.
# boolean isTarget() Returns true if the robot is currently on the target cell. Otherwise, it returns false.
# Note that direction in the above functions should be a character from {'U','D','L','R'}, representing the directions up, down, left, and right, respectively.

# Return the minimum total cost to get the robot from its initial starting cell to the target cell. If there is no valid path between the cells, return -1.

# Sol
# First, do depth first starting from the original cell of the robot to figure out all values in grid and 
# determine whether the target cell can be reached. It the target cell cannot be reached, return -1. 
# Otherwise, use a priority queue to store the cells and the corresponding costs to be visited. 
# Once the target cell is reached, return the minimum path cost.

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        def dfs(i, j):
            nonlocal target
            if master.isTarget():
                target = (i, j)
            for dir, (a, b, ndir) in dirs.items():
                x, y = i + a, j + b
                if 0 <= x < N and 0 <= y < N and master.canMove(dir) and g[x][y] == -1:
                    g[x][y] = master.move(dir)
                    dfs(x, y)
                    master.move(ndir)

        target = (-1, -1)
        N = 200
        INF = 0x3F3F3F3F
        g = [[-1] * N for _ in range(N)]
        dirs = {
            'U': (-1, 0, 'D'),
            'D': (1, 0, 'U'),
            'L': (0, -1, 'R'),
            'R': (0, 1, 'L'),
        }
        dfs(100, 100)
        if target == (-1, -1):
            return -1
        q = [(0, 100, 100)]
        dist = [[INF] * N for _ in range(N)]
        dist[100][100] = 0
        while q:
            w, i, j = heappop(q)
            if (i, j) == target:
                return w
            for a, b, _ in dirs.values():
                x, y = i + a, j + b
                if (
                    0 <= x < N
                    and 0 <= y < N
                    and g[x][y] != -1
                    and dist[x][y] > w + g[x][y]
                ):
                    dist[x][y] = w + g[x][y]
                    heappush(q, (dist[x][y], x, y))
        return 0
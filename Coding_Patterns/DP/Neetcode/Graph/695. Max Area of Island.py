# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS , COLS = len(grid) , len(grid[0])
        visit = set()

        def dfs( r , c):
            if r not in range(ROWS) or c not in range(COLS) or grid[r][c] == 0 or (r,c) in visit:
                return 0

            visit.add((r , c))
            return (1 + dfs(r + 1 , c) + dfs(r - 1 , c) + dfs(r , c - 1) + dfs(r , c + 1))
        
        area = 0
        for i in range(ROWS):
            for j in range(COLS):
                area = max(area , dfs(i , j))
        
        return area
                        

# O( n^ 2)

## using stack

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # traveral algorithm --> DFS
        numrows = len(grid)
        numcols = len(grid[0])

        # helps us prevent out of bounds errors
        def isValid(x,y):
            return 0 <= x < numrows and 0 <= y < numcols

        # matrix keep of track of when we have visisted a node before
        # help us during our DFS traversal so we dont "step on our toes" or get into a loop
        seen = [[False for _ in range(numcols)] for _ in range(numrows)]

        # when we are looping over the neighbors of a node
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # what we are looking for and what we will return at the end of the solution
        maxSize = 0

        # loop over every element of the matrix. if we have not seen this before AND the value is not zero, then we have found a new island and we want to explore it
        for i in range(numrows):
            for j in range(numcols):
                if grid[i][j] and not seen[i][j]:
                    # the start of the DFS traversal
                    stack = [[i,j]]
                    seen[i][j] = True
                    # keep track of local size of the islands
                    curr = 1 
                    while stack:
                        x,y = stack.pop()
                        
                       
                        # start exploring this island
                        for dx,dy in directions:
                            newX = x + dx
                            newY = y + dy
                            if isValid(newX,newY) and grid[newX][newY] and not seen[newX][newY]:
                                stack.append([newX,newY])
                                seen[newX][newY] = True
                                curr +=1
                    maxSize = max(curr,maxSize)
        return maxSize



        
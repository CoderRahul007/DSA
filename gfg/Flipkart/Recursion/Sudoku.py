# https://www.youtube.com/watch?v=uyetDh-DyDg
class Solution:
    
    def solve(self, grid, row, col, cell, i, j):
        if j == 9:
            if i == 8:
                return True
            else:
                return self.solve(grid, row, col, cell, i+1, 0)
        
        if(grid[i][j]):
            return self.solve(grid, row, col, cell, i, j+1)
            
        else:
            for k in range(1,9+1):
                if (k not in row[i]) and (k not in col[j]) and (k not in cell[i//3][j//3]):
                    grid[i][j] = k
                    row[i].add(k)
                    col[j].add(k)
                    cell[i//3][j//3].add(k)
                    
                    if self.solve(grid,row,col,cell,i,j+1):
                        return True
                    
                    grid[i][j] = 0
                    row[i].remove(k)
                    col[j].remove(k)
                    cell[i//3][j//3].remove(k)
        
        return False
    
    
    def SolveSudoku(self,grid):
        row = [set() for i in range(9)]
        col = [set() for j in range(9)]
        cell = [[set() for i in range(3)] for j in range(3)]
        
        for i in range(9):
            for j in range(9):
                if grid[i][j]:
                    row[i].add(grid[i][j])
                    col[j].add(grid[i][j])
                    cell[i//3][j//3].add(grid[i][j])
        
        return self.solve(grid, row, col, cell, 0, 0)
        
    
    def printGrid(self,arr):
        for row in arr:
            print(*row, end=' ')
##################################################################################################################   
#    
def valid(grid , r , c , v):
    for i in range(9):
        if grid[r][i] == v:
            return False
        if grid[i][c] == v:
            return False
        if grid[3*(r//3) + i//3][3*(c//3) + i % 3] == v:
            return False
    return True
class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        N = len(grid)
    
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0:
                    for v in range(1 , 10):
                        if valid(grid , r ,c , v):
                            grid[r][c] = v
                            if self.SolveSudoku(grid):
                                return True
                            else:
                                grid[r][c] = 0
                    return False
        return True
        
    
    #Function to print grids of the Sudoku.    
    def printGrid(self,arr):
        for row in arr:
            print(*row, end=' ')      


# Time complexity: O(9^(n*n)). 
# For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)).
# Space Complexity: O(n*n). 
# To store the output array a matrix is needed.
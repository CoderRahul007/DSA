# Given a grid of dimension nxm where each cell in the grid can have values
#  0, 1 or 2 which has the following meaning:
# 0 : Empty cell
# 1 : Cells have fresh oranges
# 2 : Cells have rotten oranges

# We have to determine what is the minimum time required to rot all oranges.
#  A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], 
# [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 
 

# Example 1:

# Input: grid = {{0,1,2},{0,1,2},{2,1,1}}
# Output: 1
# Explanation: The grid is-
# 0 1 2
# 0 1 2
# 2 1 1
# Oranges at positions (0,2), (1,2), (2,0)
# will rot oranges at (0,1), (1,1), (2,2) and 
# (2,1) in unit time.

# Example 2:

# Input: grid = {{2,2,0,1}}
# Output: -1
# Explanation: The grid is-
# 2 2 0 1
# Oranges at (0,0) and (0,1) can't rot orange at
# (0,3).

class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
    	    n , m = len(grid) , len(grid[0])
    	    q = []
    	    for i in range(n):
    	        for j in range(m):
    	            if grid[i][j] == 2:
    	                q.append([i , j])
    	    
    	    c = 0
    	    while q:
    	        loop = len(q)
    	        flag = False
    	        
    	        for _ in range(loop):
    	            i , j = q.pop(0)
    	            if i-1 >= 0 and grid[i-1][j] == 1:
    	                grid[i-1][j] = 2
    	                q.append([i-1 , j])
    	                flag = True
    	            if i+1 < n and grid[i+1][j] == 1:
    	                grid[i+1][j] = 2
    	                q.append([i+1 , j])
    	                flag = True
    	            if j-1 >= 0 and grid[i][j-1] == 1:
    	                grid[i][j-1] = 2
    	                q.append([i , j-1])
    	                flag = True
    	            if j+1 < m and grid[i][j+1] == 1:
    	                grid[i][j+1] = 2
    	                q.append([ i , j+1])
    	                flag = True
    	        if flag:
    	             c +=1
    	    
    	    for i in range(n):
    	        for j in range(m):
    	            if grid[i][j] == 1:
    	                return -1
    	    return c
	        
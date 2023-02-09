# Given a cost matrix cost[][] and a position (m, n) in cost[][], 
# write a function that returns cost of minimum cost path to reach (m, n) from (0, 0).
#  Each cell of the matrix represents a cost to traverse through that cell. 
#  The total cost of a path to reach (m, n) is the sum of all the costs on that path 
#  (including both source and destination). You can only traverse down, right and diagonally 
#  lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1), 
#  and (i+1, j+1) can be traversed. 
# You may assume that all costs are positive integers.

# 1) Optimal Substructure 
# The path to reach (m, n) must be through one of the 3 cells: (m-1, n-1) or (m-1, n) or (m, n-1). 
# So minimum cost to reach (m, n) can be written as “minimum of the 3 cells plus cost[m][n]”.
# minCost(m, n) = min (minCost(m-1, n-1), minCost(m-1, n), minCost(m, n-1)) + cost[m][n]

# 2) Overlapping Subproblems 
# Following is a simple recursive implementation of the MCP (Minimum Cost Path) problem. 
# The implementation simply follows the recursive structure mentioned above.  

def minCost( cost ):
    row = len(cost)
    col = len(cost[0])

    dp = [[0]*(col+1) for _ in range(row+1)]

    dp[0][0] = cost[0][0]

    for i in range(1 , col):
        dp[0][i] = dp[0][i-1] + cost[0][i]

    for i in range(1 , row):
        dp[i][0] = dp[i-1][0] + cost[i][0]     

    for i in range(1 , row) :
        for j in range(1 , col):
            dp[i][j] = cost[i][j] + min(dp[i-1][j] , dp[i][j-1])
    
    print(dp[row-1][col-1])


cost = [ [ 1, 2, 3 ],
             [ 4, 8, 2 ],
             [ 1, 5, 3 ] ]

minCost(cost)

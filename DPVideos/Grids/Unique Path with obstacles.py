# You are given an m x n integer array grid. There is a robot initially located at the top-left corner 
# (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). 
# The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes 
# cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

def spaceOptimised(obstacleGrid):
        m,n = len(obstacleGrid) , len(obstacleGrid[0])
        dp = [0]*n
        for j in range(n-1,-1,-1):
            if obstacleGrid[m-1][j]==1:
                break
            dp[j] = 1
        for i in range(len(obstacleGrid)-2,-1,-1):
            if obstacleGrid[i][n-1]==1:
                dp[n-1]=0
            for j in range(n-2,-1,-1):
                if not obstacleGrid[i][j]==1:
                    dp[j]+=dp[j+1]
                else:
                    dp[j]=0
        
        return dp[0]

def uniqueWithObstacles( obstacleGrid ):
    row = len(obstacleGrid)
    col = len(obstacleGrid[0])
    dp = [[0]*(col + 1) for _ in range(row+1)]

    # fill 1st row
    flag = False
    for i in range(col):
        if flag or obstacleGrid[0][i] == 1:
            flag = True
            dp[0][i] = 0 # set path as 0
        else:
            dp[0][i] = 1 # ther is a path

    flag = False
    for i in range(row):
        if flag or obstacleGrid[i][0] == 1:
            flag = True
            dp[i][0] = 0 # set path as 0
        else:
            dp[i][0] = 1 # ther is a path   
    
    for i in range(1 , row):
        for j in range(1, col):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else :
                dp[i][j]  = dp[i-1][j] + dp[j][i-1]
    return dp[row-1][col-1]
             
    
        


arr =  [[0,0,0],[0,1,0],[0,0,0]]
#arr = [[1]]

print(uniqueWithObstacles(arr))
# Given a gold mine of n*m dimensions. Each field in this mine contains a 
# positive integer which is the amount of gold in tons. Initially the miner
# is at first column but can be at any row. He can move only (right->,right 
# up /,right down\) that is from a given cell, the miner can move to the cell 
# diagonally up towards the right or right or diagonally down towards the right. 
# Find out maximum amount of gold he can collect. 
# Examples: 
 

# Input : mat[][] = {{1, 3, 3},
#                    {2, 1, 4},
#                   {0, 6, 4}};
# Output : 12 
# {(1,0)->(2,1)->(1,2)}

# Input: mat[][] = { {1, 3, 1, 5},
#                    {2, 2, 4, 1},
#                    {5, 0, 2, 3},
#                    {0, 6, 1, 2}};
# Output : 16
# (2,0) -> (1,1) -> (1,2) -> (0,3) OR
# (2,0) -> (3,1) -> (2,2) -> (2,3)

# Input : mat[][] = {{10, 33, 13, 15},
#                   {22, 21, 04, 1},
#                   {5, 0, 2, 3},
#                   {0, 6, 14, 2}};
# Output : 83

# https://www.geeksforgeeks.org/gold-mine-problem/

# Method 1: Recursion

# A simple method that is a direct recursive implementation 

# Python program to solve Gold Mine problem
def collectGold(gold, x, y, n, m):
 
    # Base condition.
    if ((x < 0) or (x == n) or (y == m)): 
        return 0
 
    # Right upper diagonal
    rightUpperDiagonal = collectGold(gold, x - 1, y + 1, n, m)
 
     # right
    right = collectGold(gold, x, y + 1, n, m)
 
    # Lower right diagonal
    rightLowerDiagonal = collectGold(gold, x + 1, y + 1, n, m)
 
    # Return the maximum and store the value
    return  gold[x][y] + max(max(rightUpperDiagonal, rightLowerDiagonal), right) 
 
 
def getMaxGold(gold,n,m):
 
    maxGold = 0
 
    for i in range(n):
 
        # Recursive function call for  ith row.
        goldCollected = collectGold(gold, i, 0, n, m)
        maxGold = max(maxGold, goldCollected)
 
    return maxGold
 
# Driver Code
gold = [[1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]
]
 
m,n = 4,4
print(getMaxGold(gold, n, m))


# Method 2: Memoization

# Bottom-Up Approach: The second way is to take an extra space of size m*n and start computing values of states 

# of right, right upper diagonal, and right bottom diagonal and store it in the 2d array.

# Python3 program to solve Gold Mine problem
def collectGold(gold, x, y, n, m, dp):
 
    # Base condition.
    if ((x < 0) or (x == n) or (y == m)):
        return 0
 
    if(dp[x][y] != -1):
        return dp[x][y]
 
    # Right upper diagonal
    rightUpperDiagonal = collectGold(gold, x - 1, y + 1, n, m, dp)
 
        # right
    right = collectGold(gold, x, y + 1, n, m, dp)
 
    # Lower right diagonal
    rightLowerDiagonal = collectGold(gold, x + 1, y + 1, n, m, dp)
 
    # Return the maximum and store the value
    dp[x][y] = gold[x][y] + max(max(rightUpperDiagonal, rightLowerDiagonal), right)
    return dp[x][y]
  
 
def getMaxGold(gold,n,m):
 
    maxGold = 0
    # Initialize the dp vector
    dp = [[-1 for i in range(m)]for j in range(n)]
     
    for i in range(n):
 
        # Recursive function call for  ith row.
        goldCollected = collectGold(gold, i, 0, n, m, dp) 
        maxGold = max(maxGold, goldCollected)
 
    return maxGold
 
# Driver Code
 
gold = [ [1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2] ]
m,n = 4,4
print(getMaxGold(gold, n, m))

# Method 3: Using Dp, Tabulation
# Create a 2-D matrix goldTable[][]) of the same as given matrix mat[][]. If we observe the question closely, we can notice following. 
 

# Amount of gold is positive, so we would like to cover maximum cells of maximum values under given constraints.
# In every move, we move one step toward right side. So we always end up in last column. If we are at the last column, then we are unable to move right

# If we are at the first row or last column, then we are unable to move right-up so just assign 0 otherwise assign the value of goldTable[row-1][col+1] to right_up. If we are at the last row or last column, then we are unable to move right down so just assign 0 otherwise assign the value of goldTable[row+1][col+1] to right up. 
# Now find the maximum of right, right_up, and right_down and then add it with that mat[row][col]. At last, find the maximum of all rows and first column and return it.
 


MAX = 100
 
# https://www.youtube.com/watch?v=hs0lilfJ7C0
# Returns maximum amount of
# gold that can be collected
# when journey started from
# first column and moves
# allowed are right, right-up
# and right-down
def getMaxGold(gold, m, n):
 
    # Create a table for storing
    # intermediate results
    # and initialize all cells to 0.
    # The first row of
    # goldMineTable gives the
    # maximum gold that the miner
    # can collect when starts that row
    goldTable = [[0 for i in range(n)]
                        for j in range(m)]
 
    for col in range(n-1, -1, -1):
        for row in range(m): # from 1st till last row
 
            # Gold collected on going to
            # the cell on the right(->)
            if (col == n-1):  # last row right not possible
                right = 0
            else:
                right = goldTable[row][col+1] 
 
            # Gold collected on going to
            # the cell to right up (/)
            if (row == 0 or col == n-1):
                right_up = 0
            else:
                right_up = goldTable[row-1][col+1]
 
            # Gold collected on going to
            # the cell to right down (\)
            if (row == m-1 or col == n-1):
                right_down = 0
            else:
                right_down = goldTable[row+1][col+1]
 
            # Max gold collected from taking
            # either of the above 3 paths
            goldTable[row][col] = gold[row][col] + max(right, right_up, right_down)
                                                            
    # The max amount of gold
    # collected will be the max
    # value in first column of all rows
    res = goldTable[0][0]
    for i in range(1, m):
        res = max(res, goldTable[i][0])
 
    return res
     
# Driver code
gold = [[1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]]
 
m = 4
n = 4
 
print(getMaxGold(gold, m, n))
 
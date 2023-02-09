# Given a boolean 2D array of n x m dimensions where each row is sorted.
#  Find the 0-based index of the first row that has the maximum number of 1's.

# Example 1:

# Input: 
# N = 4 , M = 4
# Arr[][] = {{0, 1, 1, 1},
#            {0, 0, 1, 1},
#            {1, 1, 1, 1},
#            {0, 0, 0, 0}}
# Output: 2
# Explanation: Row 2 contains 4 1's (0-based
# indexing).

# To solve in O(N + M) start from the top right corner of the matrix and keep track
#  of the index of the row which has maximum 1s. 
# Go left if you encounter 1
# Go down if you encounter 0
# Stop when you reach the last row or first column. 

def rowWithMax1s(arr, n, m):
    # code here
    i = 0
    j = m-1
    index = -1
    c = 0
    maxCount = 0 
    
    while i < n and j >= 0:
        if arr[i][j] == 1:
            j-=1
            c+=1
        else:
            i+=1
        if c > maxCount:
            index = i
            maxCount = c
    return index

# O(n+m)
        
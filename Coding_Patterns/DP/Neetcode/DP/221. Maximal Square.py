# Given an m x n binary matrix filled with 0's and 1's, 
# find the largest square containing only 1's and return its area.


# Recursive
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        cache = {}
        def helper(i , j):
            if i >= r or j >= c:                
                return 0
            key = (i,j)
            if key not in cache:
                down = helper(i + 1 , j)    
                right = helper(i , j +  1)
                diag = helper(i + 1 , j + 1)
                
                cache[key] = 0
                if matrix[i][j] == '1':
                    cache[key] = 1 +  min( down , right , diag)
            return cache[key]
        helper(0 , 0)
        return max(cache.values()) ** 2
            

# DP
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        maxsqlen = 0
        nextRow = [0] * (c+1)
        currRow = [0] * (c+1)

        for i in range(r-1 , -1 , -1):
            for j in range(c-1 , -1 , -1):
            

                if matrix[i][j] == '1':

                    left = currRow[j+1]
                    diagPrev = nextRow[j+1]
                    up = nextRow[j]

                    currRow[j] = 1 + min(left , diagPrev , up)
                    maxsqlen = max(maxsqlen , currRow[j])
                else:
                    currRow[j] = 0
            nextRow = currRow

        return maxsqlen ** 2

        
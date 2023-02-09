# Given an m x n binary matrix filled with 0's and 1's, find the largest square
#  containing only 1's and return its area.

# Example 1:

# Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# Output: 4
# Example 2:


# Input: matrix = [["0","1"],["1","0"]]
# Output: 1
# Example 3:

# Input: matrix = [["0"]]
# Output: 0

###############################################################################################
# O(m * n)^2

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0

        maxsqlen = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    sqlen = 1
                    flag = True

                    while sqlen + i < n and sqlen + j < m and flag:
                        for k in range(j , sqlen + j + 1):
                            if matrix[i + sqlen][k] == '0':
                                flag = False
                                break
                        for k in range(i , sqlen + i + 1):
                            if matrix[k][sqlen + j] == '0':
                                flag = False
                                break
                        if flag:
                            sqlen += 1
                            
                    if maxsqlen < sqlen:
                        maxsqlen = sqlen

        return maxsqlen * maxsqlen

################################################################
# O(m*n)                    
# O(m*n)

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0]) 

        cache = {}
        def helper(r , c):
            if r >= n or c >= m:
                return 0
            if (r,c) not in cache:
                right = helper(r  , c+1)
                down = helper(r+1 , c)
                diag = helper(r+1 , c+1)

                cache[(r , c)] = 0
                if matrix[r][c] == '1':
                    cache[(r , c)] = 1 + min(right , down , diag)
            return cache[(r , c)]

        helper(0 , 0)
        # this recursive solution will fill the cache from right bottom
        return max(cache.values()) ** 2

# https://www.youtube.com/watch?v=6X7Ha2PrDmM        
       

###############################################################################
#
def maximalSquare(matrix):
    r = len(matrix)
    c = len(matrix[0])
    maxsqlen = 0
    dp = [[0 for j in range(c+1)] for i in range(r+1)]

    for i in range(1 , r+1):
        for j in range(1 , c+1):
            if matrix[i-1][j-1] == '1':

                currRowPrevCol = dp[i][j - 1]
                prevRowSameCol = dp[i - 1][j]
                diagPrevious = dp[i - 1][j - 1]

                dp[i][j] = 1 + min( currRowPrevCol , prevRowSameCol , diagPrevious )

                maxsqlen = max(maxsqlen , dp[i][j])
    return maxsqlen ** 2

# O(m*n)                
# O(m*n)

#################################################################################

# public class Solution {
#     public int maximalSquare(char[][] matrix) {
#         int rows = matrix.length, cols = rows > 0 ? matrix[0].length : 0;
#         int[] dp = new int[cols + 1];
#         int maxsqlen = 0, prev = 0;
            # prev is the diag prev
#         for (int i = 1; i <= rows; i++) {
#             for (int j = 1; j <= cols; j++) {
#                 int temp = dp[j];
#                 if (matrix[i - 1][j - 1] == '1') {
#                     dp[j] = Math.min(Math.min(dp[j - 1], prev), dp[j]) + 1;
#                     maxsqlen = Math.max(maxsqlen, dp[j]);
#                 } else {
#                     dp[j] = 0;
#                 }
#                 prev = temp;
#             }
#         }
#         return maxsqlen * maxsqlen;
#     }
# }
# O(m*n)                
# O(n)


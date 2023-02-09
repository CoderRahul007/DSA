# https://www.youtube.com/watch?v=OCz6rm9Nh1o

# Given a NxN matrix of positive integers. There are only three possible moves from a cell Matrix[r][c].

#     Matrix [r+1] [c]
#     Matrix [r+1] [c-1]
#     Matrix [r+1] [c+1]

# Starting from any column in row 0 return the largest sum of any of the paths up to row N-1.

# Example 1:

# Input: N = 2
# Matrix = {{348, 391},
#           {618, 193}}
# Output: 1009
# Explaination: The best path is 391 -> 618. 
# It gives the sum = 1009.


# Example 2:

# Input: N = 2
# Matrix = {{2, 2},
#           {2, 2}}
# Output: 4
# Explaination: No matter which path is 
# chosen, the output is 4.

class Solution:
    def maximumPath(self, N, mat):
        # code here
        for i in range(1 , N):
            for j in range(N):
                a = 0
                b = 0
                c = mat[i-1][j]
                if j-1 >= 0:
                    a = mat[i-1][j-1]
                if j+1 < N:
                    b = mat[i-1][j+1]
                mat[i][j] += max(a, b , c)
        return max(mat[N-1])
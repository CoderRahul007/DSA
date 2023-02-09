# Given two n x n binary matrices mat and target, return true if it is
#  possible to make mat equal to target by rotating mat in 90-degree increments, or false otherwise.


# Example 1:

# Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
# Output: true
# Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
# Example 2:


# Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
# Output: false
# Explanation: It is impossible to make mat equal to target by rotating mat.

# Approach
# Brute Force Approach

# The first approach that comes to mind, is to rotate the matrix and compare it with 
# the target matrix whether they are equal or not, We can repeat the above process 4 times 
# as after 4 times the matrix will repeat itself. The time complexity for this approach 
# is O(4*n*n). Here we are traversing the matrix 4 times to rotate it, Can it be done using
#  only a single traversal, Let’s see!
# Optimal Approach

# We can do this in a single traversal, In a single traversal, we can compare 
# all the four rotations possible, unlike the above approach in which we are traversing the matrix 4 times.

# Conditions for four rotations:

#     matrix[i][j] = target[i][j], if given matrix is equal to target.
#     matrix[i][j] = target[j][n-1-i] , if the given matrix is rotated clckwise , 1 time.
#     matrix[i][j] = target[n-1-i][n-1-j] , if given matrix is rotated clockwise , 2 times.
#     matrix[i][j] = target[n-1-j][i] , it the given matrix is rotated clockwise , 3 times.

# If we check the above 4 conditions in one traversal, then we have checked all the possible rotations,
#  if any of them is true means a target is possible.

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        m = len(mat[0])
        check = [True] *4
        for i in range(n):
            for j in range(m):
                if mat[i][j] != target[i][j]:
                    check[0] = False
                if mat[i][j] != target[n-j-1][i]:
                    check[1] = False
                if mat[i][j] != target[n-1-i][n-1-j]:
                    check[2] = False
                if mat[i][j] != target[j][n-1-i]:
                    check[3] = False
        return any(check)
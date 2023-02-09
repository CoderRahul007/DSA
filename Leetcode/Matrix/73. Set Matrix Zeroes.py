# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

 

# Example 1:


# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Example 2:


# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Basic idea is to reuse the space in the matrix which is to be setted as 0.


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        R = len(matrix)
        C = len(matrix[0])
        rows, cols = set(), set()

        # Essentially, we mark the rows and columns that are to be made zero
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        # Iterate over the array once again and using the rows and cols sets, update the elements
        for i in range(R):
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0

# Complexity Analysis

# Time Complexity: O(M X N)

# Space Complexity: O(M+N)

######################################################################################################
# https://takeuforward.org/data-structure/set-matrix-zero/
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        col = True
        
        for i in range(n):
            if matrix[i][0] == 0:
                col = False
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0   # store the respective 0th row and 0th column to 0
					
        for i in range(n-1,-1,-1):
            for j in range(1, m):
                # print(i,j)
                if matrix[i][0] == 0 or matrix[0][j] == 0: # if the  0th row and 0th column is 0
                    matrix[i][j] = 0
            if col == False:
                matrix[i][0] = 0

# Complexity Analysis

# Time Complexity: O 2*(M X N)                
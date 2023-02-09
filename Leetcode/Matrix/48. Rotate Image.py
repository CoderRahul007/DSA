# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify 
# the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Example 2:


# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# the idea is to go from outer layer to more inside layers.
# for example, if matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 
# the outermost layer is comprised of 1,2,3,4,8,12,16,15,14,13,9,5; the inside layer is 6,7,11,10; etc.
# This method is actually more efficient than the 
# 'first reverse up to down, then swap the symmetry' method because no element will swapped more than once.

# https://pythontutor.com/render.html#mode=display

# [~i] is way nicer than [n-1-i].
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i] # swap top left element with bottom left element
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j] # swap bottom left element with right bottom element
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i] # swap bottom right element with top right element 
                matrix[j][n-1-i] = temp # top right element will be the temp i.e top left element

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
#  This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
def findTarget(matrix, target):
    for i in range(len(matrix)):
        start = 0
        end = len(matrix[i]) - 1

        while start <= end:
            mid = (start+end)//2

            if matrix[i][mid] == target:
                return True

            elif matrix[i][mid] < target:
                start = mid+1
            else:
                end = mid-1
    return False

# O(row * (log col) )
############################################################################


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) < 1 or len(matrix[0]) < 1:
            return False
        for row in matrix:
            if row[0] > target:
                return False
            elif row[len(row)-1] < target:
                continue
            else:
                l = 0
                r = len(row) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] < target:
                        l = mid + 1
                    elif row[mid] > target:
                        r = mid - 1
                    else:
                        return True
        return False
###############################################################


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows-1

    # the time complexity of this solution is
        while bottom >= 0 and top < cols:
            if matrix[bottom][top] == target:
                return True
            if matrix[bottom][top] < target:
                top += 1
            else:
                bottom -= 1
        return False

# Given an n x n matrix where each of the rows and columns is sorted in ascending order,
# return the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# You must find a solution with a memory complexity better than O(n2).


# Example 1:

# Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
# Output: 13
# Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
# Example 2:

# Input: matrix = [[-5]], k = 1
# Output: -5

# Using maxheap
import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                heapq.heappush(heap, -matrix[row][col])
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heapq.heappop(heap)
# O(mnlogk)


# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/solutions/2393717/python-o-n-log-max-min-solution-no-extra-log-n-factor/?languageTags=python&topicTags=binary-search

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]  # min, max

        def findIndex(matrix, val):
            '''
            Returns Position where val can be inserted in O(m + n).
                        All nums to right of result position will be >= val
            '''
            addAt = 0
            m, n = 1, len(matrix[0])
            while m < len(matrix) + 1 and n > 0:
                if matrix[m - 1][n - 1] >= val:
                    n -= 1
                else:
                    addAt += n
                    m += 1
            addAt += 1
            return addAt
        while lo < hi:
            mid = (lo + hi)//2
            if findIndex(matrix, mid) > k:
                hi = mid
            else:
                lo = mid + 1
        if findIndex(matrix, lo) <= k:
            return lo
        return lo - 1

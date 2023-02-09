# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# https://leetcode.com/problems/pascals-triangle-ii/discuss/1323926/Various-solutions-with-python-implementation

# Solution#1 - Using Recursion
# We can get the jth element in ith row using the following recurrence:
# Recurrence: f(i, j) = f(i-1, j-1) + f(i-1, j)
# Base cases: f(0, j) = f(i, 0) = f(i, j) = 1
# We have to use memoization/caching to save repeated work
# Time Complexity: O(n^2) where n = rowIndex
# It computes all the values of the pascal triangle upto the row queried.
# Space Complexity: O(n)
# Stores only the required row.
# I believe stack space used is also O(n) as at any time there won't be more than n recursive calls in the stack

def getRow(self, rowIndex: int) -> List[int]:
    
    @cache
    def get(i,j):
        if i == 0 or j == 0 or j == i: return 1
        return get(i-1,j-1) + get(i-1,j)
    
    return [get(rowIndex,j) for j in range(rowIndex+1)]

# Solution#2 - Iterative
# Same approach as the recursive solution, but implemented in an iterative way.
# Time Complexity: O(n^2) where n = rowIndex
# Two nested O(n) for loops
# Space Complexity: O(n)
# Stores only the required row.

def getRow(self, rowIndex: int) -> List[int]:
    row = [1]*(rowIndex+1)
    for i in range(1, rowIndex):
        for j in range(i, 0, -1):
            row[j] = row[j-1] + row[j]
    return row
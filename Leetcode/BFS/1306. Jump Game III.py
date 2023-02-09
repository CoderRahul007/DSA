# Given an array of non-negative integers arr, you are initially positioned at start index
# of the array. When you are at index i, you can jump to i + arr[i] or i - arr[i],
# check if you can reach to any index with value 0.

# Notice that you can not jump outside of the array at any time.


# Example 1:

# Input: arr = [4,2,3,0,3,1,2], start = 5
# Output: true
# Explanation:
# All possible ways to reach at index 3 with value 0 are:
# index 5 -> index 4 -> index 1 -> index 3
# index 5 -> index 6 -> index 4 -> index 1 -> index 3
# Example 2:

# Input: arr = [4,2,3,0,3,1,2], start = 0
# Output: true
# Explanation:
# One possible way to reach at index 3 with value 0 is:
# index 0 -> index 4 -> index 1 -> index 3
# Example 3:

# Input: arr = [3,0,2,1,2], start = 2
# Output: false
# Explanation: There is no way to reach at index 1 with value 0.

###################################################################################
# DFS
class Solution(object):
    def canReach(self, arr, start):
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        self.seen = dict()
        
        def back(pos):
            if pos < 0 or pos >= len(arr) or pos in self.seen:
                return False
            
            if arr[pos] == 0:
                return True
            
            self.seen[pos] = True
            return back(pos + arr[pos]) or back(pos - arr[pos])
    
        return back(start)




##################################################################################
# BFS

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = [0]*n
        lst = [start]
        visited[start] = 1
        while lst:
            x = lst.pop(0)
            if arr[x] == 0:
                return True
            if x + arr[x] < n and visited[x + arr[x]] == 0:
                lst.append(x + arr[x])
                visited[x + arr[x]] = 1
            if x - arr[x] >= 0 and visited[x - arr[x]] == 0:
                lst.append(x - arr[x])
                visited[x - arr[x]] = 1
        return False

# You are given a 0-indexed binary string s and two integers minJump and maxJump.
#  In the beginning, you are standing at index 0, which is equal to '0'. 
#  You can move from index i to index j if the following conditions are fulfilled:

# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

# Example 1:

# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.
# Example 2:

# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false

# Initial thought: brute force and do exactly what the problem says:

# Create a queue of reachable indices starting with 0
# While the queue is not empty, pull from front of queue, call this i
# Let x go from i + minJumps to i + maxJumps, if s[x] == '0', add to queue
# Repeat till queue is empty or reached end
# If reached end return true, if queue empty, return false
# We realize that this solution is O(n^2) since maxJump-minJump can be as big as n. 
# But actually, we are close to the solution: notice that we are repeatedly adding in indices that have been visited.

# For example, consider s = "0100000", minJumps = 2, maxJumps = 6. After the first iteration, 
# we have already put all the relevant indices into the queue. When we visit index 2,
#  we can start adding the next reachable indices from where the last iteration leftoff
#   (there are none left in this case). I keep track of where to start with the max_reached variable.

# Let n = length of s
# Time complexity: O(n), we visit each index at most twice - once to add to queue, and once to pop it out
# Space complexity: O(n), in the worst case we can have almost all of the indices of s
#  in the queue at once. For example s = "0000000", minJumps = 1, maxJumps = 6. 
#  After one iteration, queue = [1,2,3,4,5,6]

import collections
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q, max_reached = collections.deque([0]), 0
        while q:
            curr_i = q.popleft()
            if curr_i == len(s) - 1:
                return True
            start = max(curr_i + minJump, max_reached + 1)
            for i in range(start, min(curr_i + maxJump + 1, len(s))):
                if s[i] == '0':
                    q.append(i)
            max_reached = curr_i + maxJump
        return False


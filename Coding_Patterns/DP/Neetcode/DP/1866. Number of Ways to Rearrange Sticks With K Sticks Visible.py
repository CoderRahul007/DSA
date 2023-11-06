# There are n uniquely-sized sticks whose lengths are integers from 1 to n.
#  You want to arrange the sticks such that exactly k sticks are visible from the left.
#  A stick is visible from the left if there are no longer sticks to the left of it.

# For example, if the sticks are arranged [1,3,2,5,4], then the sticks with lengths 1, 3,
#  and 5 are visible from the left.
# Given n and k, return the number of such arrangements. Since the answer may be large, 
# return it modulo 109 + 7.

 

# Example 1:

# Input: n = 3, k = 2
# Output: 3
# Explanation: [1,3,2], [2,3,1], and [2,1,3] are the only arrangements such that exactly 2 sticks are visible.
# The visible sticks are underlined.
# Example 2:

# Input: n = 5, k = 5
# Output: 1
# Explanation: [1,2,3,4,5] is the only arrangement such that all 5 sticks are visible.
# The visible sticks are underlined.
# Example 3:

# Input: n = 20, k = 11
# Output: 647427950
# Explanation: There are 647427950 (mod 109 + 7) ways to rearrange the sticks such that exactly 11 sticks are visible.

# take example of [1  2  3] , n = 3 ,k = 2
# lets for each ele check if we can achieve by placing it in the last 
# by placing 1 at the last firstly -> [ 2 , 3 , 1] or [ 3 , 2 , 1] so here the subproblem become  n = 2 , k = 2 
# by placing 2 at the last firstly -> [ 1 , 3 , 2] or [ 3 , 1 , 2] so here the subproblem become  n = 2 , k = 2 
# by placing 3 at the last firstly -> [ 1 , 2 , 3] or [ 2 , 1 , 3] so here the subproblem become  n = 2 , k = 1 , here k = 1 since 3 will always be visible
# as long we are placing the not the greatest element at the last of the array it wont be visible 
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = {}
        def dfs(N ,K):
            if N == 0 or K == 0:
                return 0
            if N == K:
                return 1
            key = (N , K)
            if key in dp:
                return dp[key]
            
            dp[key] = dfs(N -1 , K - 1) + (N - 1) * dfs(N - 1 , K)
            return dp[key]
        return dfs(n , k) % (10 ** 9 + 7)

###############################

from collections import defaultdict
class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        dp = defaultdict(int)
        dp[(1 , 1)] = 1
        for N in range(2 , n+1):
            for K in range(1 , k+1):
                dp[(N,K)] = dp.get((N - 1 , K - 1) , 0) + (N - 1) * dp.get((N - 1 , K) , 0)
        return dp[(n , k)]% (10 ** 9 + 7)
        
# O(n * k)
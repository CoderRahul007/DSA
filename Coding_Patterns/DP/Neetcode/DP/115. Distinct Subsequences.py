# Given two strings s and t, return the number of distinct
# subsequences
#  of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit
# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            key = (i, j)

            if key in dp:
                return dp[key]

            if s[i] == t[j]:
                dp[key] = ( dfs(i + 1, j + 1) # if matched then i and j are both increased
                        + dfs(i + 1, j) ) # if matched i then we see beyyond i if it can be matched
            else:
                dp[key] = dfs(i + 1, j) # didnt matched so we increase the i
            return dp[key]

        return dfs(0, 0)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [1] + [0] * len(t)
        for i in range(len(s) - len(t) + 1):
            for j in range(len(t)):
                if s[i + j] == t[j]:
                    dp[j + 1] += dp[j]
        return dp[-1]

# O(n*m)
# Space - O(n*m)

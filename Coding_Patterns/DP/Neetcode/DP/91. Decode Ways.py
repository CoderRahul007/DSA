# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped
#  into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.


# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


class Solution:
    def numDecodings(self, s: str) -> int:
        def recursive(s, i, validNums, n, memo):
            if i in memo:
                return memo[i]
            if i == n:
                return 1
            if s[i] == '0':
                return 0
            ans1 = ans2 = 0

            if s[i] in validNums:
                ans1 = recursive(s, i+1, validNums, n, memo)
            if i < n-1 and (s[i] + s[i+1] in validNums):
                ans2 = recursive(s, i+2, validNums, n, memo)
            memo[i] = ans1 + ans2
            return memo[i]

        validNums = {str(i) for i in range(1, 27)}
        n = len(s)
        memo = {}

        return recursive(s, 0, validNums, n, memo)


############################################
# Dp

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = { len(s): 1 }
        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if (i + 1 < len(s) and (10 <= int(s[i] + s[i + 1]) < 27)):
                dp[i] += dp[i + 2]
        return dp[0]

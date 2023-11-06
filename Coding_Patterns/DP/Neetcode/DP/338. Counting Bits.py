# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            target = i
            c = 0
            while target:
                c += 1 if target & 1 else 0
                target = target // 2
            ans.append(c)
        return ans

# O(n log n)            

###############################

class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1
        for i in range(1 , n + 1):
            if 2 * offset == i:
                offset = i
            dp[i] = 1 + dp[ i - offset]
        return dp

            
# the above approach is based on the pattern we found that from 0 to 3 the pattern repeats for an offset i.3 from 4 to 8
# so we are calculating offset based on a number 2 * offset if its equal we reached a new offset
# https://www.youtube.com/watch?v=RyBM56RIWrM&list=PLot-Xpze53lcvx_tjrr_m2lgD2NsRHlNO&index=33

# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.

class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        return self.squtil(n, int(n**0.5), memo)
                
    def squtil(self, n, sn, memo):
        min_cnt = 0
        
        if (n, sn) in memo:
            return memo[(n, sn)]
        
        for num in range(sn, 0, -1):
            sq = num * num
            
            if sq * 4 <= n:
                break
            
            rest = n
            sq_cnt = 0
            
            while rest >= sq:
                rest = rest - sq
                sq_cnt += 1

            cnt = self.squtil(rest, int(rest**0.5), memo) + sq_cnt

            if cnt < min_cnt or min_cnt == 0:
                min_cnt = cnt

        memo[(n, sn)] = min_cnt
        
        return min_cnt
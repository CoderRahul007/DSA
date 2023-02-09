# The bitwise AND of an array nums is the bitwise AND of all integers in nums.

#     For example, for nums = [1, 5, 3], the bitwise AND is equal to 1 & 5 & 3 = 1.
#     Also, for nums = [7], the bitwise AND is 7.

# You are given an array of positive integers candidates. Evaluate the bitwise AND of every combination of numbers of candidates. Each number in candidates may only be used once in each combination.

# Return the size of the largest combination of candidates with a bitwise AND greater than 0.

 

# Example 1:

# Input: candidates = [16,17,71,62,12,24,14]
# Output: 4
# Explanation: The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0.
# The size of the combination is 4.
# It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0.
# Note that more than one combination may have the largest size.
# For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

# Example 2:

# Input: candidates = [8,8]
# Output: 2
# Explanation: The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0.
# The size of the combination is 2, so we return 2.

# If 'n' numbers ANDs up with each other to result in a number > 0, then there must be atleast one bit set to True for all the 'n' numbers.
# Reason: This is how AND works. If anyone of the bit is 0, then the whole AND result for that particular bit is zero.

# Approach:

#     Iterate through each bit for each number and count the number of 1.
#     Return the max count of ones considering each bit for all the numbers.

# The full code (written during contest) is given below:

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0
        for bit in range(32):
            count = 0
            for i in range(len(candidates)):
                if candidates[i] & (1<<(31 - bit)) == 0:
                    continue
                count += 1
            ans = max(ans, count)
        return ans

# Time and Space Complexity Analysis:
# We see here nothing but two loops of size '32' and 'n' both nested together 
# (simultaneous). Hence, time complexity = O(32 * n) = O(n) . Right??

# NOPE !!!!!!!!!!!!!!!!!!

# Reason, here 32 is not just a constant, it comes because ideally integer is of 32 bits.
#  If integer were of 64 bits, then we would have looped for 64 times.

# So, clearly this is not a constant. It is what it is... O(32 * n). But one more thing
#  this can be mapped to is log2(10^9) = 30 (nearly).
# So, time complexity can be said as O(nlogn).

# Space complexity = Constant = O(1) as no extra variable sized memory is used.



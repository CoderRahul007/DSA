# Given a positive integer n, find out how many ways of writing n as a sum of positive integers. Two sums that differ only in the order of their summands are considered the same partition.

# Example:

# Input: 5
# Output: 6
# Explanation:
# 1. 1 + 1 + 1 + 1 + 1
# 2. 1 + 1 + 1 + 2
# 3. 1 + 1 + 3
# 4. 1 + 4
# 5. 1 + 2 + 2
# 6. 2 + 3

class Solution:
    def UniquePartitions(self, n):
    # Code here
        table =[0] * (n + 1) 
        table[0] = 1
        for i in range(1, n ): 
            for j in range(i , n + 1): 
                table[j] +=  table[j - i]  
        return table[n] 
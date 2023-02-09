# You are given two positive integers n and target.

# An integer is considered beautiful if the sum of its digits is less than or equal to target.

# Return the minimum non-negative integer x such that n + x is beautiful.
#  The input will be generated such that it is always possible to make n beautiful.

# Example 1:

# Input: n = 16, target = 6
# Output: 4
# Explanation: Initially n is 16 and its digit sum is 1 + 6 = 7.
#  After adding 4, n becomes 20 and digit sum becomes 2 + 0 = 2. 
#  It can be shown that we can not make n beautiful with adding non-negative integer less than 4.
# Example 2:

# Input: n = 467, target = 6
# Output: 33
# Explanation: Initially n is 467 and its digit sum is 4 + 6 + 7 = 17.
#  After adding 33, n becomes 500 and digit sum becomes 5 + 0 + 0 = 5. 
#  It can be shown that we can not make n beautiful with adding non-negative integer less than 33.
# Example 3:

# Input: n = 1, target = 1
# Output: 0
# Explanation: Initially n is 1 and its digit sum is 1, which is already smaller than or equal to target.

######################################################################################################
class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        #function for finding the sum of the digits of a number
        def digit_sum(n):
            return sum([int(c) for c in str(n)])
        
        lst = 1 # the number of zeros we want to leave at the end
        add = 0
        
        #A problem for one idea: 
        #if the sum of digits is greater than target, it is most optimal to make the last few digits equal to zero
        
        while digit_sum(n + add) > target:
            x = 10 ** lst
            add = x - n % x
            lst += 1
        
        return add
        #O(n * lg(n)) - Time
        #O(1) - Space

###########################################################################################################

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:

        sm = lambda x: sum(int(digit) for digit in str(x))

        zeros, diff = 10, 0                     #  Ex: n = 5617     ; target = 7

        while sm(n + diff) > target:            #   n    zeros   diff  n+diff  sm(n+diff)
                                                # -----  –––––  –––––  ––––––  –––––––––  
            diff = zeros - n % zeros              # 5617     10      3    5620     13  
                                                # 5617    100     83    5700     12
            zeros *= 10                          # 5617   1000    383    6000      6  <-- less than target
                                                #                 |
        return diff                             #               answer
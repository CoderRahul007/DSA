# Given an integer array nums where every element appears three times except for one, 
# which appears exactly once. Find the single element and return it.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

 

# Example 1:

# Input: nums = [2,2,3,2]
# Output: 3
# Example 2:

# Input: nums = [0,1,0,1,0,1,99]
# Output: 99


# Implementation by by python built-in Counter:

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
		# key: number
		# value: occurrennce
        num_occ_dict = Counter( nums )
        
        return [ number for number in num_occ_dict if num_occ_dict[number] == 1][0]


# Implementation by bit masking with O(1) aux space:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single_num = 0
        
        # compute single number by bit masking
        for bit_shift in range(32):
            
            sum = 0
            
            for number in nums:
                
                # collect the bit sum
                sum += ( number >> bit_shift ) & 1

            # Extract bit information of single number by modulo
            # Other number's bit sum is removed by mod 3 (i.e., all other numbers appear three times)
            single_num |= ( sum % 3 ) << bit_shift
            
            
        
        if ( single_num & (1 << 31) ) == 0:
            return single_num
        else:
			# handle for negative number
            return -( (single_num^(0xFFFF_FFFF))+1 )

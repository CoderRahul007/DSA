# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9


# # O(nlogn)
# O(1) here O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = length = 0
        lis = sorted(set(nums))
        prev = lis[0]
        for i in lis[1:]:
            if i==prev+1:
                length += 1
            else:
                length  = 0
            if length>res:
                res = length
            prev = i
        return res+1
                                    


# TC -> O(n)
# SC -> O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        ans = 1
        #processed = set()
        snums = set(nums)
        for num in nums:
            #if num not in processed and num-1 not in snums:
            if num-1 not in snums:
                #processed.add(num)
                curr_ans = 1
                curr_num = num+1
                while curr_num in snums:
                    #processed.add(curr_num)
                    curr_ans += 1
                    curr_num += 1
                ans = max(ans,curr_ans)

        return ans
        
        
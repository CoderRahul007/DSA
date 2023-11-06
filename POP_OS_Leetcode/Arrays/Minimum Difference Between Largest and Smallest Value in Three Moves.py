import sys
class Solution:
    def minDifference(self, nums):
        n=len(nums)
        k=3
        if (n<k+2):
            return 0
        sort(nums)
        m=-sys.maxsize
        for i in range(k+1):
            m=min(nums[n-1-i]-nums[k-i],m)
        return m


# two pointers
# class Solution:
#     def minDifference(self, nums: List[int]) -> int:
       
#         if len(nums) <= 4:
#             return 0
        
#         # Two Pointers
# 		nums.sort()
#         right, left = 0, len(nums) - 1
		
#         # There are only 3 steps we can do
#         for i in range(3, 0, -1):
		
#             # Compare right_diff & left_diff
# 			# right_diff & left_diff is the max difference that can be removed given i steps left
#             right_diff = nums[right + i] - nums[right]
#             left_diff = nums[left] - nums[left - i]
#             if right_diff >= left_diff:
#                 right += 1
#             else:
#                 left -= 1
                
#         return nums[left] - nums[right]
s=Solution()
print(s.minDifference( [6,6,0,1,1,4,6]))dd

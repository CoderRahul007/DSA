# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

# Example 1:

# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        
        if not nums: return 0
        
        f = [0] * len(nums) # max
        g = [0] * len(nums) # min
        res = float('-inf')
        
        for i in range(len(nums)):
            if i == 0:
                f[i] = nums[i]
                g[i] = nums[i]
                res = max(res, f[i])
                continue
                
            if nums[i] > 0:
                f[i] = max(nums[i] * f[i-1], nums[i]) # nums[i] > 0, then times the largest, otherwise smallest
            else:
                f[i] = max(nums[i] * g[i-1], nums[i])

            res = max(res, f[i])
            
            if nums[i] > 0:
                g[i] = min(nums[i] * g[i-1], nums[i]) # opposite to f[i]
            else:
                g[i] = min(nums[i] * f[i-1], nums[i])
        
        return res

#=--------------------------------------------------------
import sys
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=-sys.maxsize
        s=1
        for i in nums:
            s*=i
            if s>m:
                m=s
            if s==0:
                s=1    
        s=1
        for i in nums[::-1]: # [3,-1,4] to check from the last 
            s*=i
            if s>m:
                m=s
            if s==0:
                s=1
        return m

# class Solution {
#     public int maxProduct(int[] nums) {
#         int i,p=1;
#         int max=Integer.MIN_VALUE;
#         if(nums.length<=1)
#             return nums[0];
#         for(i=0;i<nums.length;i++)
#         {
#             p=p*nums[i];
#             if(p>max)
#                 max=p;
#              if(p==0)
#                  p=1;
#          }
#         p=1;
#          for(i=nums.length-1;i>=0;i--)
#         {
#             p=p*nums[i];
#              if(p>max)
#                 max=p;
#              if(p==0)
#                  p=1;
#         }
#         return max;
        
#     }
# }
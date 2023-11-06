# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

# Example: 

# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.

# Follow up:
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 


# Two Pointer solution
import sys
class Solution:
    def minSubArrayLen(self, s, nums):
        if not nums:
            return 0
        
        n=len(nums)
        ans=sys.maxsize
        l=0
        sum=0
        for i in range(n):
            sum+=nums[i]
            print('Sum+=Nums',sum)
            while sum>=s:
                print('i',i)
                print('i+1-l',i+1-l)
                print('Ans',ans)
                ans=min(ans,(i+1-l))
                sum-=nums[l]
                print('Sum',sum)
                l+=1
                print('l+1',l)
            print('------------------')
        print('last',sum)
        if ans!=sys.maxsize:
            return ans
        else:
            return 0
        
# Binary Search Solution
# import bisect
# class Solution:
#     def minSubArrayLen(self, s, nums):
#         cum=[] # positive elements, thus cummulative is incremental and never duplicate
#         summ=0
#         ans=float('inf')
#         for i,num in enumerate(nums):
#             summ+=num
#             diff=summ-s
#             print('diff','summ',diff,summ)
#             if diff >=0:
#                 j=bisect.bisect_right(cum,diff)
#                 print('j',j)
#                 length=i-(j-1)
#                 print('len',length)
#                 ans=min(ans,length)
#                 print('ans',ans)
#             cum.append(summ)
#         return 0 if ans==float('inf') else ans
s=Solution()
print(s.minSubArrayLen(7,[2,3,1,2,4,3]))

# Most of the solutions I saw here use two nested loops. Though it doesn't increase the time complexity, 
# I believe a O(n) solution should be solved using only 1 loop. In nested loop solutions, the inner loop of the solution is used to 
# increase the left pointer i. e. to shrink the window. In my solution, I am taking a decision in each iteration wether to shrink the
#  window or to expand the window (increase the right pointer). I am checking if the current sum is greater then the required sum beacause 
# even if the right pointer is out of bounds, the last element may be contributing to the sum and hence the left pointer can still be decreased.
#  Hence there are two conditions in the loop that must be checked.
# For example in this case 5 is contributing to the solution.

# 11
# [1,2,3,4,5]

# This is the solution with two loops

# public int minSubArrayLen(int s, int[] a) {
#   if (a == null || a.length == 0)
#     return 0;
  
#   int i = 0, j = 0, sum = 0, min = Integer.MAX_VALUE;
  
#   while (j < a.length) {
#     sum += a[j++];
    
#     while (sum >= s) {
#       min = Math.min(min, j - i);
#       sum -= a[i++];
#     }
#   }
  
#   return min == Integer.MAX_VALUE ? 0 : min;
# }

# This is the solution I propose

# class Solution {
#     public int minSubArrayLen(int s, int[] nums) {
#         if (nums.length == 0)
#             return 0;
#         int left = 0;
#         int right = 0;
#         int sum = 0;
#         int min = Integer.MAX_VALUE;
#         while (sum >= s || right < nums.length) {
#             if (sum >= s) {
#                 min = Math.min(min, right - left);
#                 sum -= nums[left++];
#             }
#             else {
#                 sum += nums[right++];
#             }
#         }
#         return min == Integer.MAX_VALUE ? 0 : min;
#     }
# }


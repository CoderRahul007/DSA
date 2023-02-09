# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

# https://leetcode.com/problems/maximum-product-subarray/solutions/2781113/kadane-s-algo-for-maximum-product-subarray/

########################################
# Wrong

# class Solution {
#     public int maxProduct(int[] nums) {
#          int currentPro=Integer.MIN_VALUE;
#         int prevPro=1;

#         for(int i =0; i<nums.length; i++){
#             prevPro*=nums[i];
          
#             if(prevPro> currentPro){
#                 currentPro=prevPro;
#             }
#             if(prevPro<0){
#                 prevPro=1;
#             }
#         }
      
#         return currentPro;
#     }
# }

# Normal Kadane Algo Fails bcz

# But failed because
# Two negative numbers are added to make negative number but if two negative numbers 
# are multiplied to make a positive number

# Thus, I need
# To take care of the current product (which is maximum product now) and the previous
#  product (which became minimum product)

# if negative number comes say -1 and suppose if current product =4 (max) and previous product = -2 (min)

# then 4 * (-1) = - 4 and -2 * (-1) = 2

# Due to negative number, minproduct becomes max and maxproduct becomes minimum.

# If I use this maxproduct (which has became minimum) then the answer will be wrong because
#  I want maximum product to update the answer

# Thus, I need to swap the min and max products so that the minimum product will give me 
# the maximum value and I can use this value to update the answer.

# So, technically while explaining to interviewer, you can say that this is the variation
#  of Kadane's algo. But the difference is that for max-sum subarray we were taking care 
# of the maxsum but here, we need to take care of maxproduct as well as minproduct because
#  minproduct helps to eliminate the problem of (-) + (-) = (+) in the array

# TC= O(n) and SC=O(1)
# class Solution {
#    public int maxProduct(int[] nums) {
#        int maxPro=nums[0];
#        int minPro=nums[0];
#        int answer = nums[0];

#        for(int i =1; i<nums.length; i++){
#            if(nums[i]<0){
#                // if next is -1 and maxpro=4 then 4 x -1 = -4 which is minimum 
#                // thus swap maxPro and minPro
#                int temp=maxPro;
#                maxPro=minPro;
#                minPro=temp;  
#            }
#    // maxproduct 
#             maxPro= Math.max( maxPro*nums[i],   nums[i]);
#    // minimum product 
#             minPro= Math.min( minPro*nums[i], nums[i]);
            
#             answer=Math.max(answer, maxPro);
            
#        }
     
#        return answer;
#    }
# }

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        minPro = nums[0]
        maxPro = nums[0]

        for i in range(1 , len(nums)):
            if nums[i] < 0:
                maxPro , minPro = minPro , maxPro
            maxPro = max( maxPro * nums[i] , nums[i])
            minPro = min(minPro * nums[i]  , nums[i])
            ans = max(ans , maxPro)
        return ans


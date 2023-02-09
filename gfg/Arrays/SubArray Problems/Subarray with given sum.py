# Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

# In case of multiple subarrays, return the subarray which comes first on moving from left to right.

 

# Example 1:

# Input:
# N = 5, S = 12
# A[] = {1,2,3,7,5}
# Output: 2 4
# Explanation: The sum of elements 
# from 2nd position to 4th position 
# is 12.


#Sliding window 

class Solution:
    def subArraySum(self,arr, n, s): 
       #Write your code here
        left = 0
        curr_sum = 0
        for right in range(len(arr)):
            curr_sum += arr[right]
           
            while curr_sum > s:
               curr_sum -= arr[left]
               left += 1
            if curr_sum == s:
                return (left +1 , right +1)
        return [-1]
            
    # Time Complexity : O(n). 
    #     The Array is traversed only once to insert elements into the window. It will take O(N) time
    #     The Array is traversed again once to remove elements from the window. It will also take O(N) time.
    #     So the total time will be O(N) + O(N) = O(2*N), which is similar to O(N)
    # Space Complexity: O(1). 
    # As constant extra space is required.
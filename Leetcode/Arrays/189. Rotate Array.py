# Given an array, rotate the array to the right by k steps, where k is non-negative.

 

# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# https://leetcode.com/problems/rotate-array/solutions/2747423/complete-python-explanation-5-methods/

# https://leetcode.com/problems/rotate-array/solutions/1730142/java-c-python-a-very-very-well-detailed-explanation/

# We have k is 3, so it means we have to take 3 values from the back and put in the front of the array values.

# This is a great solution but crazily there is one way to reduce the space complexity further!
# To do this, we need a special insight about how to rotate the array. We want the last k elements 
# to become the first k elements of our array, so how about we begin by reversing the whole list.
# After that, the first k elements will be last k elements of our original list, but they will
# be in reverse order. Similarly, the new end of our list will be the old beginning, only in
# reverse order. So how do we remedy this? Well, we can reverse the first k elements of our
# new array and the last n-k elements! After that, the array will be fully rotated!

# Method 5: Reverse; Time: O(n), Space: O(1)

def rotate(self, nums: List[int], k: int) -> None:
	def reverse(start, end): # helper method to reverse from start to end
		while start < end: # while there is stuff to reverse
			nums[start], nums[end] = nums[end], nums[start] # swap the elements at the ends
			start, end = start + 1, end - 1 # move pointers closer to each other
			
	n = len(nums)
	k %= n
	reverse(0,n-1) # reverse full list
	reverse(0,k-1) # reverse first k elements (previously the last k elements)
	reverse(k,n-1) # reverse the rest of the list

# If you are still confused about how this works, I'll show what nums looks like
#  after each step with the example problems:

# Example 1

# original nums: [1, 2, 3, 4, 5, 6, 7]
# nums after fully reversing: [7, 6, 5, 4, 3, 2, 1]
# nums after reversing the first k elements: [5, 6, 7, 4, 3, 2, 1]
# nums after reversing the remaining elements: [5, 6, 7, 1, 2, 3, 4]
# Example 2

# original nums: [-1, -100, 3, 99]
# nums after fully reversing: [99, 3, -100, -1]
# nums after reversing the first k elements: [3, 99, -100, -1]
# nums after reversing the remaining elements: [3, 99, -1, -100]


##############################################################################
# What if k is negative

# Okay Bonus point what if we have k = -1, then how can we rotate the array.
#  If k is -1 then we have to rotate the value backward not in the front.
# Eg - 
# Input : [1,2,3,4,5,6,7], k = -1
# Output : [2,3,4,5,6,7,1]

# Now how did we figure out this, if you carefully look that k = -1 is equals to k = 6.
# Just look at the table which I have made for every possible k values

# So, what It represent is that add the -ve value to the length of array. And you will get your answer!

class Solution:
    def reverse (self, nums, i, j) : 
        li = i
        ri = j
        
        while li < ri:
            nums[li] , nums[ri] = nums[ri] , nums[li]                        
            li += 1
            ri -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % len(nums)
        if k < 0 : 
            k += len(nums)
        
        self.reverse(nums, 0, n - k - 1) # sort ele before last k elements
        self.reverse(nums, n - k, n - 1) # sort last k element
        self.reverse(nums, 0, n - 1) # sort whole array
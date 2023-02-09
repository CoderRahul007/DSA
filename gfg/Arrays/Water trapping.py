# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

# Examples:  

# Input: arr[]   = {2, 0, 2}
# Output: 2

# Input: arr[]   = {3, 0, 2, 0, 4}
# Output: 7

# Basic Insight: 
# An element of the array can store water if there are higher bars on the left and right. 
# The amount of water to be stored in every element can be found out by finding the heights of bars on the left
#  and right sides. The idea is to compute the amount of water that can be stored in every element of the array. 

# Example 
# Consider the array {3, 0, 2, 0, 4}, three units of water can be stored in three indexes 1 and 2,
#  and one unit of water at index 3, and three units of water at index 4. 

# For Array[] = {3, 0, 2, 0, 4} 
# Water stored = 0 + 3 + 1 + 3 + 0 = 7 

# Python3 implementation of the approach

# Function to return the maximum
# water that can be stored
def maxWaterHigherComplexity(arr, n) :
	
	# To store the maximum water
	# that can be stored
	res = 0
	
	# For every element of the array
	for i in range(1, n - 1) :
		
		# Find the maximum element on its left
		left = arr[i]
		for j in range(i) :
			left = max(left, arr[j])
		
		# Find the maximum element on its right
		right = arr[i]
		
		for j in range(i + 1 , n) :
			right = max(right, arr[j])
			
		# Update the maximum water
		res = res + (min(left, right) - arr[i])

	return res

# Driver code
# Python program to find maximum amount of water that can
# be trapped within given set of bars.

def findWaterHigherSpaceComplexity(arr, n):

	# left[i] contains height of tallest bar to the
	# left of i'th bar including itself
	left = [0]*n

	# Right [i] contains height of tallest bar to
	# the right of ith bar including itself
	right = [0]*n

	# Initialize result
	water = 0

	# Fill left array
	left[0] = arr[0]
	for i in range( 1, n):
		left[i] = max(left[i-1], arr[i])

	# Fill right array
	right[n-1] = arr[n-1]
	for i in range(n-2, -1, -1):
		right[i] = max(right[i + 1], arr[i])

	# Calculate the accumulated water element by element
	# consider the amount of water on i'th bar, the
	# amount of water accumulated on this particular
	# bar will be equal to min(left[i], right[i]) - arr[i] .
	for i in range(0, n):
		water += min(left[i], right[i]) - arr[i]

	return water


# Python3 implementation of the approach

# Function to return the maximum
# water that can be stored

# https://www.youtube.com/watch?v=C8UjlJZsHBw
def maxWaterOptimised(arr, n):
	# indices to traverse the array
	left = 0
	right = n-1

	# To store Left max and right max
	# for two pointers left and right
	l_max = 0
	r_max = 0

	# To store the total amount
	# of rain water trapped
	result = 0
	while (left <= right):
		
		# We need check for minimum of left
		# and right max for each element
		if r_max <= l_max:
			
			# Add the difference between
			#current value and right max at index r
			result += max(0, r_max-arr[right])
			
			# Update right max
			r_max = max(r_max, arr[right])
			
			# Update right pointer
			right -= 1
		else:
			
			# Add the difference between
			# current value and left max at index l
			result += max(0, l_max-arr[left])
			
			# Update left max
			l_max = max(l_max, arr[left])
			
			# Update left pointer
			left += 1
	return result





arr = [0, 1, 0, 2, 1, 0,1, 3, 2, 1, 2, 1]
n = len(arr)
print(maxWaterHigherComplexity(arr, n)) # O(n^2)
print(findWaterHigherSpaceComplexity(arr , n)) # O(n) space is O(n)
print(maxWaterOptimised(arr , n)) # O(n) and space O(1)



# Problem Statement
# You have been given a long type array/list 'ARR' of size 'N'. 
# It represents an elevation map wherein 'ARR[i]' denotes the elevation of the 'ith' bar. 
# Print the total amount of rainwater that can be trapped in these elevations.
# Note :

# The width of each bar is the same and is equal to 1.
def getTrappedWater(arr, n) :
	# Write your code here.
        if n <= 1:
            return 0
        lmax = 0
        rmax = 0
        i = 0
        j = n-1
        water = 0
        while i < j :
            lmax = max(lmax , arr[i])
            rmax = max(rmax ,  arr[j])
            if lmax < rmax : # shortest one will be used for calculating water level
                water += (lmax-arr[i])
                i+=1
            else:
                water += (rmax - arr[j])
                j-=1
        return water

################################
# Python program to find maximum amount of water that can
# be trapped within given set of bars.

def findWater(arr, n):

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


# Driver program

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print("Maximum water that can be accumulated is", findWater(arr, n))

####################################################################################################
# We can use a Stack to track the bars that are bounded by the longer left and right bars. 
# This can be done using only one iteration using stacks.

# Approach:

# 1. Loop through the indices of the bar array.

# 2. For each bar, we can do the following:

# While the Stack is not empty and the current bar has a height greater than the top bar of the stack,
# Store the index of the top bar in pop_height and pop it from the Stack.
# Find the distance between the left bar(current top) of the popped bar and the current bar.
# Find the minimum height between the top bar and the current bar.
# The maximum water that can be trapped in distance * min_height.
# The water trapped, including the popped bar, is (distance * min_height) – height[pop_height].
# Add that to the fans.
# 3. Final answer will the ans.

##########################################################################################################
# Python implementation of the approach
  
# Function to return the maximum
# water that can be stored
def maxWater(height):
      
    # Stores the indices of the bars
    stack = []
      
    # size of the array
    n = len(height)
      
    # Stores the final result
    ans = 0
      
    # Loop through the each bar
    for i in range(n):
          
        # Remove bars from the stack
        # until the condition holds
        while(len(stack) != 0 and (height[stack[-1]] < height[i]) ):
              
            # store the height of the top
            # and pop it.
            pop_height = height[stack[-1]]
            stack.pop()
              
            # If the stack does not have any
            # bars or the popped bar
            # has no left boundary
            if(len(stack) == 0):
                break
              
            # Get the distance between the
            # left and right boundary of
            # popped bar
            distance = i - stack[-1] - 1
              
            # Calculate the min. height
            min_height = min(height[stack[-1]],height[i])-pop_height
              
            ans += distance * min_height
          
        # If the stack is either empty or
        # height of the current bar is less than
        # or equal to the top bar of stack
        stack.append(i)
      
    return ans
  
# Driver code
arr=[ 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(maxWater(arr))
  
# This code is contributed by rag2127
# Output
# 6
# Time Complexity: O(n)
# Auxiliary Space: O(n) 
#########################################################################################################
# Method 5 (Two Pointer Approach)

# Approach: At every index, The amount of rainwater stored is the difference between
#  the current index height and a minimum of left max height and right max-height
# Algorithm :
# Take two pointers l and r. Initialize l to the starting index 0 and r to the last index n-1
# Since l is the first element, left_max would be 0, and right max for r would be 0
# While l <= r, iterate the array. We have two possible conditions
# Condition1 : left_max <= right max
# Consider Element at index l
# Since we have traversed all elements to the left of l, left_max is known 
# For the right max of l, We can say that the right max would  always be >= current r_max here
# So, min(left_max,right_max) would always equal to left_max in this case
# Increment l
# Condition2 : left_max >  right max
# Consider Element at index r
# Since we have traversed all elements to the right of r, right_max is known
# For the left max of l, We can say that the left max would  always be >= current l_max here
# So, min(left_max,right_max) would always equal to right_max in this case
# Decrement r
# Implementation:

# Python3 implementation of the approach
  
# Function to return the maximum
# water that can be stored
  
  
def maxWater(arr, n):
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
  
  
# Driver code
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = len(arr)
print(maxWater(arr, n))
  
# This code is contributed by Nikhil Chatragadda
# Output
# 6
# Time Complexity: O(n)
# Auxiliary Space: O(1) 

# https://www.geeksforgeeks.org/trapping-rain-water/
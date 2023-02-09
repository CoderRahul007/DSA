# Given n numbers (both +ve and -ve), arranged in a circle, find the maximum sum of consecutive numbers. 

# Examples: 

# Input: a[] = {8, -8, 9, -9, 10, -11, 12}
# Output: 22 (12 + 8 - 8 + 9 - 9 + 10)

# Input: a[] = {10, -3, -4, 7, 6, 5, -4, -1} 
# Output:  23 (7 + 6 + 5 - 4 -1 + 10) 

# Input: a[] = {-1, 40, -14, 7, 6, 5, -4, -1}
# Output: 52 (7 + 6 + 5 - 4 - 1 - 1 + 40)

# Method 1 There can be two cases for the maximum sum:  

# Case 1: The elements that contribute to the maximum sum are arranged such that no wrapping is there. 
# Examples: {-10, 2, -1, 5}, {-2, 4, -1, 4, -1}. 
# In this case, Kadane’s algorithm will produce the result.
# Case 2: The elements which contribute to the maximum sum are arranged such that wrapping is there.
#  Examples: {10, -12, 11}, {12, -5, 4, -8, 11}. In this case, we change wrapping to non-wrapping.
#   Let us see how. Wrapping of contributing elements implies non-wrapping of non-contributing elements, 
#   so find out the sum of non-contributing elements and subtract this sum from the total sum. 
#    find out the sum of non-contributions, invert the sign of each element and then run Kadane’s algorithm. 
# Our array is like a ring and we have to eliminate the maximum continuous negative that implies
# maximum continuous positive in the inverted arrays. Finally, we compare the sum obtained in both
# cases and return the maximum of the two sums.

# Python program for maximum contiguous circular sum problem


# Standard Kadane's algorithm to find maximum subarray sum
def kadane(a):
	Max = a[0]
	temp = Max
	for i in range(1,len(a)):
		temp += a[i]
		if temp < a[i]:
			temp = a[i]
		Max = max(Max,temp)
	return Max

# The function returns maximum circular contiguous sum in
# a[]
def maxCircularSum(a):

	n = len(a)

	# Case 1: get the maximum sum using standard kadane's
	# algorithm
	max_kadane = kadane(a)

	# Case 2: Now find the maximum sum that includes corner
	# elements.
	# You can do so by finding the maximum negative contiguous
	# sum
	# convert a to -ve 'a' and run kadane's algo
	neg_a = [-1*x for x in a]
	max_neg_kadane = kadane(neg_a)

	# Max sum with corner elements will be:
	# array-sum - (-max subarray sum of inverted array)
	max_wrap = -(sum(neg_a)-max_neg_kadane)

	# The maximum circular sum will be maximum of two sums
	res = max(max_wrap,max_kadane)
	return res if res != 0 else max_kadane



# Python program for maximum contiguous circular sum problem

# Method 2 
# Approach: In this method, modify Kadane’s algorithm to find a minimum contiguous subarray sum and the
#  maximum contiguous subarray sum, then check for the maximum value between the max_value and the value 
# left after subtracting min_value from the total sum.
# Algorithm 

#     We will calculate the total sum of the given array.
#     We will declare the variable curr_max, max_so_far, curr_min, min_so_far as the first value of the array.
#     Now we will use Kadane’s Algorithm to find the maximum subarray sum and minimum subarray sum.
#     Check for all the values in the array:- 
#         If min_so_far is equaled to sum, i.e. all values are negative, then we return max_so_far.
#         Else, we will calculate the maximum value of max_so_far and (sum – min_so_far) and return it.

def maxCircularSumComplete(a, n):
	
	# Corner Case
	if (n == 1):
		return a[0]

	# Initialize sum variable which
	# store total sum of the array.
	sum = 0
	for i in range(n):
		sum += a[i]

	
	curr_max = a[0]
	max_so_far = a[0]
	curr_min = a[0]
	min_so_far = a[0]


	for i in range(1, n):
	
		# Kadane's Algorithm to find Maximum subarray sum.
		curr_max = max(curr_max + a[i], a[i])
		max_so_far = max(max_so_far, curr_max)

		# Kadane's Algorithm to find Minimum subarray sum.
		curr_min = min(curr_min + a[i], a[i])
		min_so_far = min(min_so_far, curr_min)
		
	# boundary casse if all elements are negative  then min_so_far will be sum so give the max_so_far means highest negative number		
	if (min_so_far == sum):
		return max_so_far

	# returning the maximum value
	# sum - min_so_far gives the max value so take the max of it
	return max(max_so_far, sum - min_so_far)

# Driver code
a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
n = len(a)
print("Maximum circular sum is", maxCircularSumComplete(a, n))

# This code is contributes by subhammahato348

# a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
a = [ -1 , -2 , -3 , -4]
print ("Maximum circular sum is", maxCircularSum(a))


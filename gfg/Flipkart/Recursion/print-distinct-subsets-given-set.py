# Approach: The idea is simple, that if there are n number of elements inside an array, 
# there are two choices for every element. Either include that element in the subset or do not include it. 
# Using the above idea forms a recursive solution to the problem.
# Algorithm: 
 

# Create a recursive function that takes the following parameters, input array, 
# the current index, the output array, or current subset, if all the subsets need
#  to be stored then a vector of the array is needed if the subsets need to be 
#  printed only then this space can be ignored.
# if the current index is equal to the size of the array, then print the subset or 
# output array or insert the output array into the vector of arrays (or vectors) and return.
# There are exactly two choices for very index.
# Ignore the current element and call the recursive function with the current subset 
# and next index, i.e i + 1.
# Insert the current element in the subset and call the recursive function with the
#  current subset and next index, i.e i + 1.

# Python3 program to find all subsets
# by backtracking.

# In the array A at every step we have two
# choices for each element either we can
# ignore the element or we can include the
# element in our subset
def subsetsUtil(A, subset, index):
	print(*subset)
	for i in range(index, len(A)):
		
		# include the A[i] in subset.
		subset.append(A[i])
		
		# move onto the next element.
		subsetsUtil(A, subset, i + 1)
		
		# exclude the A[i] from subset and
		# triggers backtracking.
		subset.pop(-1)
	return

# below function returns the subsets of vector A.
def subsets(A):
	global res
	subset = []
	
	# keeps track of current element in vector A
	index = 0
	subsetsUtil(A, subset, index)
	
# Driver Code

# find the subsets of below vector.
array = [1, 2, 3]

# res will store all subsets.
# O(2 ^ (number of elements inside array))
# because at every step we have two choices
# either include or ignore.
subsets(array)


# Time Complexity: O(n(2 ^ n)). 
# For every index i two recursive cases originate, So Time Complexity is O(2^n).
#  If we include the time taken to copy the subset vector into the res vector the 
#  time taken will be equal to the size of the subset vector.
# Space Complexity: O(n). 
# The space complexity can be reduced if the output array is not stored and the
#  static and global variable is used to store the output string.
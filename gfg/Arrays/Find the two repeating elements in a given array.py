# You are given an array of n+2 elements. All elements of the array are in range 1 to n. And all elements occur once except two numbers which occur twice. Find the two repeating numbers. 

# Example:

#     Input: 
#     arr = [4, 2, 4, 5, 2, 3, 1] 
#     n = 5
#     Output:
#     4 2
#     Explanation:
#     The above array has n + 2 = 7 elements with all elements occurring once except 2 and 4 which occur twice. So the output should be 4 2.


# Let the repeating numbers be X and Y, if we xor all the elements in the array and all integers from 1 to n, then the result is X xor Y. 
# The 1’s in binary representation of X xor Y is corresponding to the different bits between X and Y. Suppose that the kth bit of X xor Y is 1,
#  we can xor all the elements in the array and all integers from 1 to n, whose kth bits are 1. The result will be one of X and Y. 

# Python3 code to Find the
# two repeating elements
# in a given array
def printRepeating(arr, size):
	
	# Will hold xor
	# of all elements
	xor = arr[0]
	n = size - 2
	x = 0
	y = 0
	
	# Get the xor of all
	# elements in arr[]
	# and 1, 2 .. n
	for i in range(1 , size):
		xor ^= arr[i]
	for i in range(1 , n + 1):
		xor ^= i
	
	# Get the rightmost set
	# bit in set_bit_no
	set_bit_no = xor & ~(xor-1)
	
	# Now divide elements in two
	# sets by comparing rightmost
	# set bit of xor with bit at
	# same position in each element.
	for i in range(0, size):
		
		if(arr[i] & set_bit_no):
			
			# XOR of first
			# set in arr[]
			x = x ^ arr[i]
		else:
			
			# XOR of second
			# set in arr[]
			y = y ^ arr[i]
			
	for i in range(1 , n + 1):

		if(i & set_bit_no):
			
			# XOR of first set
			# in arr[] and
			# 1, 2, ...n
			x = x ^ i
		else:
			
			# XOR of second set
			# in arr[] and
			# 1, 2, ...n
			y = y ^ i
			
	print("The two repeating",
		"elements are", y, x)

# Driver code
arr = [4, 2, 4,
	5, 2, 3, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)


# Method 5 (Use array elements as index) 
# Thanks to Manish K. Aasawat for suggesting this method. 

# Traverse the array. Do following for every index i of A[].
# {
# check for sign of A[abs(A[i])] ;
# if positive then
#    make it negative by   A[abs(A[i])]=-A[abs(A[i])];
# else  // i.e., A[abs(A[i])] is negative
#    this   element (ith element of list) is a repetition
# }

# Example: A[] =  {1, 1, 2, 3, 2}
# i=0; 
# Check sign of A[abs(A[0])] which is A[1].  A[1] is positive, so make it negative. 
# Array now becomes {1, -1, 2, 3, 2}

# i=1; 
# Check sign of A[abs(A[1])] which is A[1].  A[1] is negative, so A[1] is a repetition.

# i=2; 
# Check sign of A[abs(A[2])] which is A[2].  A[2] is  positive, so make it negative. '
# Array now becomes {1, -1, -2, 3, 2}

# i=3; 
# Check sign of A[abs(A[3])] which is A[3].  A[3] is  positive, so make it negative. 
# Array now becomes {1, -1, -2, -3, 2}

# i=4; 
# Check sign of A[abs(A[4])] which is A[2].  A[2] is negative, so A[4] is a repetition.

# Note that this method modifies the original array and may not be a recommended method if we are not allowed to modify the array. 

# Python3 code for Find the two repeating
# elements in a given array


def printRepeating(arr, size) :
	
	print(" The repeating elements are",end=" ")
	
	for i in range(0,size) :
		
		if(arr[abs(arr[i])] > 0) :
			arr[abs(arr[i])] = (-1) * arr[abs(arr[i])]
		else :
			print(abs(arr[i]),end = " ")

# Driver code
arr = [4, 2, 4, 5, 2, 3, 1]
arr_size = len(arr)
printRepeating(arr, arr_size)


# This code is contributed by Nikita Tiwari.

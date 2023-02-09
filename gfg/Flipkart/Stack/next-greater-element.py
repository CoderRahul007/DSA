# https://www.geeksforgeeks.org/next-greater-element/

# Given an array, print the Next Greater Element (NGE) for every element. 
# The Next greater Element for an element x is the first greater element on 
# the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1. 

# Examples: 

# For an array, the rightmost element always has the next greater element as -1.
# For an array that is sorted in decreasing order, all elements have the next greater element as -1.
# For the input array [4, 5, 2, 25], the next greater elements for each element are as follows.
# Element       NGE
#    4      -->   5
#    5      -->   25
#    2      -->   25
#    25     -->   -1
# d) For the input array [13, 7, 6, 12}, the next greater elements for each element are as follows.  

#   Element        NGE
#    13      -->    -1
#    7       -->     12
#    6       -->     12
#    12      -->     -1

# Method 2 (Using Stack) 

# Push the first element to stack.
# Pick rest of the elements one by one and follow the following steps in loop. 
# Mark the current element as next.
# If stack is not empty, compare top element of stack with next.
# If next is greater than the top element, Pop element from stack. 
# next is the next greater element for the popped element.
# Keep popping from the stack while the popped element is smaller than next. 
# next becomes the next greater element for all such popped elements.
# Finally, push the next in the stack.
# After the loop in step 2 is over, pop all the elements from the stack and 
# print -1 as the next element for them.

###################################################################################################

# Python code to implement the approach

# prints element and NGE pair for all
# elements of arr[] of size n
def printNGE(arr, n):

	s = []
	res = [0 for i in range(n)]

	# iterate for rest of the elements
	for i in range(n-1,-1,-1):

		# /* if stack is not empty, then
		# pop an element from stack.
		# If the popped element is smaller
		# than next, then
		# a) print the pair
		# b) keep popping while elements are
		# smaller and stack is not empty */
		if (len(s) != 0):
			while (len(s) != 0 and s[-1] <= arr[i]):
				s.pop()
		res[i] = -1 if len(s) == 0 else s[-1]
		s.append(arr[i])

	for i in range(len(arr)):
		print(str(arr[i]) + " --> " + str(res[i]))
	
# Driver Code
arr = [ 11, 13, 21, 3 ]
n = len(arr)

# Function call
printNGE(arr, n)

#####################################################################################################################
# Method 3:

# 1. This is same as above method but the elements are pushed and popped only once into the stack.
#  The array is changed in place. The array elements are pushed into the stack until it finds a 
#  greatest element in the right of array. In other words the elements are popped from stack when 
#  top of the stack value is smaller in the current array element.

# 2. Once all the elements are processed in the array but stack is not empty. The left out elements
#  in the stack doesn’t encounter any greatest element . So pop the element from stack and change
#  it’s index value as -1 in the array.

class Solution:
	def nextLargerElement(self,arr,n):
		#code here
		s=[]
		for i in range(len(arr)):
			while s and s[-1].get("value") < arr[i]:
				d = s.pop()
				arr[d.get("ind")] = arr[i]
			s.append({"value": arr[i], "ind": i})
		while s:
			d = s.pop()
			arr[d.get("ind")] = -1
		return arr
		
if __name__ == "__main__":
	print(Solution().nextLargerElement([6,8,0,1,3],5))

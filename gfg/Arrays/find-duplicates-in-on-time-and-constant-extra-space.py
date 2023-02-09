# Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times. Find these repeating numbers in O(n) and using only constant memory space.

# Example: 

# Input : n = 7 and array[] = {1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6

# Explanation: The numbers 1 , 3 and 6 appears more
# than once in the array.

# Input : n = 5 and array[] = {1, 2, 3, 4 ,3}
# Output: 3

# Explanation: The number 3 appears more than once
# in the array.

# Python3 code to find duplicates in O(n) time


# Approach: The basic idea is to use a HashMap to solve the problem. But there is a catch, the numbers in the array are from 0 to n-1, and the input array has length n. So, the input array can be used as a HashMap. While Traversing the array, if an element ‘a’ is encountered then increase the value of a%n‘th element by n. The frequency can be retrieved by dividing the a % n’th element by n.
# Algorithm: 
#     Traverse the given array from start to end.
#     For every element in the array increment the arr[i]%n‘th element by n.
#     Now traverse the array again and print all those indexes i for which arr[i]/n is greater than 1. Which guarantees that the number n has been added to that index
#     This approach works because all elements are in the range from 0 to n-1 and arr[i] would be greater than n only if a value “i” has appeared more than once.


numRay = [0, 4, 3, 2, 7, 8, 2, 3, 1]
arr_size = len(numRay)
for i in range(arr_size):

	x = numRay[i] % arr_size
	numRay[x] = numRay[x] + arr_size

print("The repeating elements are : ")
for i in range(arr_size):
	if (numRay[i] >= arr_size*2):
		print(i, " ")

# This code is contributed by 29AjayKumar

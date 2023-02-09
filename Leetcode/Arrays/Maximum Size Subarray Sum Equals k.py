# Problem:

# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
#  If there isn't one, return 0 instead.

# Note: The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

# Example 1: Given nums = [1, -1, 5, -2, 3], k = 3, return 4. (because the subarray [1, -1, 5, -2]
#  sums to 3 and is the longest)

# Example 2: Given nums = [-2, -1, 2, 1], k = 1, return 2. (because the subarray [-1, 2] 
# sums to 1 and is the longest)

# Follow Up: Can you do it in O(n) time?

# Python3 implementation to find the length
# of longest subArray having sum k

# function to find the longest
# subarray having sum k
def lenOfLongSubarr(arr, n, k):

	# dictionary mydict implemented
	# as hash map
	mydict = dict()

	# Initialize sum and maxLen with 0
	sum = 0
	maxLen = 0

	# traverse the given array
	for i in range(n):

		# accumulate the sum
		sum += arr[i]

		# when subArray starts from index '0'
		if (sum == k):
			maxLen = i + 1

		# check if 'sum-k' is present in
		# mydict or not
		elif (sum - k) in mydict:
			maxLen = max(maxLen, i - mydict[sum - k])

		# if sum is not present in dictionary
		# push it in the dictionary with its index
		if sum not in mydict:
			mydict[sum] = i

	return maxLen

# Driver Code
if __name__ == '__main__':
	arr = [10, 5, 2, 7, 1, 9]
	n = len(arr)
	k = 15
	print("Length =", lenOfLongSubarr(arr, n, k))


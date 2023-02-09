# Given a set of integers, find distinct sum that can be generated from the subsets of the given sets.
 
# https://www.geeksforgeeks.org/find-distinct-subset-subsequence-sums-array/
# Example 1:

# Input: nums = {1,2}
# Output: {1,2,3}
# Explanation: Three distinict sum can be
# calulated which are 1, 2 and 3.

# Example 2:

# Input: nums = {1,2,3}
# Output: {1,2,3,4,5,6}
# Explanation: Six distinict sum can be calculated
# which are 1, 2, 3, 4, 5 and 6.

##########################################################################3
# Naive
# Python 3 program to print distinct subset sums of
# a given array.

# sum denotes the current sum of the subset
# currindex denotes the index we have reached in
# the given array
def distSumRec(arr, n, sum, currindex, s):
	if (currindex > n):
		return

	if (currindex == n):
		s.add(sum)
		return

	distSumRec(arr, n, sum + arr[currindex], currindex+1, s)
	distSumRec(arr, n, sum, currindex+1, s)

# This function mainly calls recursive function
# distSumRec() to generate distinct sum subsets.
# And finally prints the generated subsets.
def printDistSum(arr,n):
	s = set()
	distSumRec(arr, n, 0, 0, s)

	# Print the result
	for i in s:
		print(i,end = " ")

# Driver code
if __name__ == '__main__':
	arr = [2, 3, 4, 5, 6]
	n = len(arr)
	printDistSum(arr, n)


##############################################################################
# Dp
class Solution:
	def DistinctSum(self, arr):
		# Code here
        n = len(arr)
        Sum = sum(arr)
         
        # dp[i][j] would be true if arr[0..i-1]
        # has a subset with Sum equal to j.
        dp = [[False for i in range(Sum + 1)]
                     for i in range(n + 1)]
                      
        # There is always a subset with 0 Sum
        for i in range(n + 1):
            dp[i][0] = True
     
        # Fill dp[][] in bottom up manner
        for i in range(1, n + 1):
     
            dp[i][arr[i - 1]] = True
     
            for j in range(1, Sum + 1):
                 
                # Sums that were achievable
                # without current array element
                if (dp[i - 1][j] == True):
                    dp[i][j] = True
                    dp[i][j + arr[i - 1]] = True
                 
        # Print last row elements
        ans = []
        for j in range(Sum + 1):
            if (dp[n][j] == True ):		
                ans.append(j)
        return ans

# Time complexity of the above approach is O(n*sum)
#  where n is the size of the array and sum is the sum of all the integers in the array.
# User function Template for python3
import heapq


class Solution:
    def median(self, matrix, r, c):
        # code here
        mid = (r*c)//2 + 1
        cnt = 0
        ans = -1
        pq = []
        for i in range(r):
            heapq.heappush(pq, (matrix[i][0], i, 0))
        while cnt != mid:
            temp = heapq.heappop(pq)
            col = temp[2]
            row = temp[1]
            key = temp[0]
            if col+1 < c:
                heapq.heappush(pq, (matrix[row][col+1], row, col+1))
            ans = key
            cnt += 1
        return ans
# space- > O(r)
# time -> O(r) + r*c*log(r)
###############################################################################################
# An efficient approach for this problem is to use a binary search algorithm. 
# The idea is that for a number to be median there should be exactly (n/2) numbers 
# that are less than this number. So, we try to find the count of numbers less than
#  all the numbers. Below is the step-by-step algorithm for this approach: 

# Algorithm:  

# First, we find the minimum and maximum elements in the matrix. The minimum element can be easily found by comparing the 
# first element of each row, and similarly, the maximum element can be found by comparing the last element of each row.
# Then we use binary search on our range of numbers from minimum to maximum, we find the mid of the min and max and get 
# a count of numbers less than or equal to our mid. And accordingly change the min or max.
# For a number to be median, there should be (r*c)/2 numbers smaller than that number. So for every number, we get 
# the count of numbers less than or equal to that by using upper_bound() in each row of the matrix, if it is less 
# than the required count, the median must be greater than the selected number, else the median must be less than 
# or equal to the selected number.

# Python program to find median of matrix
# sorted row wise

from bisect import bisect_right as upper_bound

MAX = 100

# Function to find median in the matrix
def binaryMedian(m, r, d):
	mi = m[0][0]
	mx = 0
	for i in range(r):
		if m[i][0] < mi:
			mi = m[i][0]
		if m[i][d-1] > mx :
			mx = m[i][d-1]
	
	desired = (r * d + 1) // 2
	
	while (mi < mx):
		mid = mi + (mx - mi) // 2
		place = [0]
		
		# Find count of elements smaller than or equal to mid
		for i in range(r):
			j = upper_bound(m[i], mid)
			place[0] = place[0] + j
		if place[0] < desired:
			mi = mid + 1
		else:
			mx = mid
	print ("Median is", mi)
	return
	
# Driver code
r, d = 3, 3

m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]]
binaryMedian(m, r, d)

# This code is contributed by Sachin BIsht

# Time Complexity: O(32 * r * log(c)). The upper bound function will take log(c) 
# time and is performed for each row. And since the numbers will be max of 32 bit,
# so binary search of numbers from min to max will be performed in at most 32 ( log2(2^32) = 32 ) operations. 
# Auxiliary Space: O(1) 
 
# https://www.youtube.com/watch?v=mouCn3CFpgg&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=24

# let arr = [5, 8 , 7 , 1 , 9]
# take lis =[1 , 1 , 1 , 1 ,1]
# since every element is an lis of lenght 1
# A naive Python implementation of LIS problem

""" To make use of recursive calls, this function must return
two things:
1) Length of LIS ending with element arr[n-1]. We use
max_ending_here for this purpose
2) Overall maximum as the LIS may end with an element
before arr[n-1] max_ref is used this purpose.
The value of LIS of full array of size n is stored in
*max_ref which is our final result """

import sys
 
 
# Function to find the maximum sum of increasing subsequence
def LIS(nums, i=0, prev = -sys.maxsize, total = 0):
 
    # base case: nothing is remaining
    if i == len(nums):
        return total
 
    # case 1: exclude the current element and process the
    # remaining elements
    excl = LIS(nums, i + 1, prev, total)
 
    # case 2: include the current element if it is greater
    # than the previous element
    
    if nums[i] > prev: # if prev is less than current it means it can be added in subsequesnce
        incl = LIS(nums, i + 1, nums[i], total + 1)
    else: # if prev is greater than current it means it will not be added in solution
        incl = total
 
    # return the maximum of the above two choices
    return max(incl, excl)
 
 

 

def lis_from_last_element( arr , n):
    lis = [1] * n
    for i in range(n-1 , -1 , -1): # we are starting from 
        # behind since from last element we check if there is an element greater
        # than that if not lis is 1 for all
        # and we use the lis of next element to evaluate the lis of 
        # previous element and when all element are proccesed then we calculate max
        # for refernce refer neetcode
        for j in range(i+1 , n):
            if arr[i] < arr[j]:
                lis[i] = max( 1 + lis[j] , lis[i])
    m = max(lis)
    s = []
    for i in range(len(lis)):
        if lis[i] == m:
            s.append(arr[i])
            m-=1
    print(s)
        





def lis(arr):
    lis = [1]*len(arr)
    for i in range(1 , len(arr)):
        for j in range(0 , i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = 1 + lis[j]
    print(max(lis))
    m = max(lis)
    s = []
    for i in range(len(lis)-1 , -1 , -1):       
        if lis[i] == m:
            s.append(arr[i])
            m = m-1
    print(s[::-1])
# TIme O(n^2) space O(n)



# arr = [5 ,8 , 7 , 1 , 9]

arr = [10, 22, 9, 33, 21, 50, 41, 60]
lis_from_last_element(arr  , len(arr))
print(LIS(arr))
# constructPrintLIS(arr)




#### Binary Search

def Bin_LIS(arr):	
	lis = []

	for h in arr:
		left = lower_bound(lis, h)
		# left is greater than all elements in LIS
		if left == len(lis):
			lis.append(h)
		# Replace the first height that is >= than h with h
		else:
			lis[left] = h

	return len(lis)

def lower_bound(nums, h):
	l, r = 0, len(nums)-1
	lower = -1
	while l <= r:
		mid = l + (r-l) // 2
		if nums[mid] >= h:
			lower =  mid
			r = mid - 1
		else:
			l = mid + 1
	return lower
# https://www.youtube.com/watch?v=on2hvxBXJH4&t=34s

# public int lengthOfLIS(int[] nums) {
#     int n = nums.length;
#     if (n == 0) {
#         return 0;
#     }
#     int dp[] = new int[n];
#     int len = 0;
#     for (int i = 0; i < n; i++) {
#         int start = 0;
#         int end = len;
#         while (start < end) {
#             int mid = (start + end) >>> 1;
#             if (dp[mid] < nums[i]) {
#                 start = mid + 1;
#             } else {
#                 end = mid;
#             }
#         }
#         dp[start] = nums[i];
#         if (start == len) {
#             len++;
#         }
#     }
#     return len;
# }

    
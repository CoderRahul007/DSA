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

# global variable to store the maximum
global maximum


def _lis(arr, n):

	# to allow the access of global variable
	global maximum

	# Base Case
	if n == 1:
		return 1

	# maxEndingHere is the length of LIS ending with arr[n-1]
	maxEndingHere = 1

	"""Recursively get all LIS ending with arr[0], arr[1]..arr[n-2]
	IF arr[n-1] is smaller than arr[n-1], and max ending with
	arr[n-1] needs to be updated, then update it"""
	for i in range(1, n):
		res = _lis(arr, i)
		if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
			maxEndingHere = res + 1

	# Compare maxEndingHere with overall maximum. And
	# update the overall maximum if needed
	maximum = max(maximum, maxEndingHere)

	return maxEndingHere


def lisRecur(arr):

	# to allow the access of global variable
	global maximum

	# length of arr
	n = len(arr)

	# maximum variable holds the result
	maximum = 1

	# The function _lis() stores its result in maximum
	_lis(arr, n)

	return maximum


# Driver program to test the above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print ("Length of lis is ", lisRecur(arr))

def printLIS(arr: list):
    for x in arr:
        print(x, end=" ")
    print()
 
# Function to construct and print Longest Increasing
# Subsequence
def constructPrintLIS(arr):
 
    # L[i] - The longest increasing sub-sequence
    # ends with arr[i]
    n = len(arr)
    l = [[] for i in range(n)]
 
    # L[0] is equal to arr[0]
    l[0].append(arr[0])
 
    # start from index 1
    for i in range(1, n):
 
        # do for every j less than i
        for j in range(i):
 
            # L[i] = {Max(L[j])} + arr[i]
            # where j < i and arr[j] < arr[i]
            if arr[i] > arr[j] and (len(l[i]) < len(l[j]) + 1):
                l[i] = l[j].copy()
 
        # L[i] ends with arr[i]
        l[i].append(arr[i])
 
    # L[i] now stores increasing sub-sequence of
    # arr[0..i] that ends with arr[i]
    maxx = l[0]
 
    # LIS will be max of all increasing sub-
    # sequences of arr
    for x in l:
        if len(x) > len(maxx):
            maxx = x
 
    # max will contain LIS
    printLIS(maxx)

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
lis(arr)
# constructPrintLIS(arr)
    
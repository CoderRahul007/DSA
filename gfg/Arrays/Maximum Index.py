# Given an array A[] of N positive integers. The task is to find the maximum of j - i
#  subjected to the constraint of A[i] < A[j] and i < j.
 

# Example 1:

# Input:
# N = 2
# A[] = {1, 10}
# Output:
# 1
# Explanation:
# A[0]<A[1] so (j-i) is 1-0 = 1.

# Example 2:

# Input:
# N = 9
# A[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
# Output:
# 6
# Explanation:
# In the given array A[1] < A[7]
# satisfying the required 
# condition(A[i] < A[j]) thus giving 
# the maximum difference of j - i 
# which is 6(7-1).


#   https://www.geeksforgeeks.org/given-an-array-arr-find-the-maximum-j-i-such-that-arrj-arri/

# Python3 program to find the maximum
# j – i such that arr[j] > arr[i]

# For a given array arr[], returns
# the maximum j – i such that
# arr[j] > arr[i]


def maxIndexDiff(arr, n):
	maxDiff = -1
	for i in range(0, n):
		j = n - 1
		while(j > i):
			if arr[j] > arr[i] and maxDiff < (j - i):
				maxDiff = j - i
			j -= 1

	return maxDiff



arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)


def Onlogn(a, n):
    # To store the index of an element.
    index = dict()
    for i in range(n):
        if a[i] in index:

            # append to list (for duplicates)
            index[a[i]].append(i)
        else:

            # if first occurrence
            index[a[i]] = [i]

    # sort the input array
    a.sort()	
    maxDiff = 0

    # Temporary variable to keep track of minimum i
    temp = n	
    for i in range(n):
        if temp > index[a[i]][0]:
            temp = index[a[i]][0]
        maxDiff = max(maxDiff, index[a[i]][-1]-temp)

    print(maxDiff)


def maxIndexDiffOrderOfN(arr, n):
    maxDiff = 0
    LMin = [0] * n
    RMax = [0] * n
 
    # Construct LMin[] such that
    # LMin[i] stores the minimum
    # value from (arr[0], arr[1],
    # ... arr[i])
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])
 
    # Construct RMax[] such that
    # RMax[j] stores the maximum
    # value from (arr[j], arr[j + 1],
    # ..arr[n-1])
    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1])
 
    # Traverse both arrays from left
    # to right to find optimum j - i
    # This process is similar to
    # merge() of MergeSort
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        if (LMin[i] <= RMax[j]):
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1
 
    return maxDiff    

# Another Approach: ( only using one extra array )

# We consider an auxiliary array : rightMax[] , such that, rightMax[i] = max element of the subarray arr[i…(n-1)], the largest or equal element after arr[i] element

# Suppose (arr[i], arr[jLast] ) is a pair, such that arr[jLast] is the last greater or equal element than arr[i]. For the pairs ending with arr[jLast] :  ( arr[k], arr[jLast] ) for all k = (i+1) to jLast

# we don’t need to consider (jLast – k) because (jLast – i ) > (jLast – k) for all such k’s.

# So we can skip those pairs.

# Traversing from left to right of both arrays : arr[] and rightMax[]  , when we first encounter rightMax[j] < arr[i[  , we know that jLast = j-1, and we can skip the pairs (arr[k], arr[jLast]) for all k = (i+1) to jLast. 

# And also rightMax[] is non increasing sequence , so all elements at right side of rightMax[j] is smaller than or equal to rightMax[j]. But there may be arr[x]  after arr[i] (x > i) such that arr[x] < rightMax[j] for x > i, so increment i when rightMax[j] < arr[i] is encountered.

# For a given array arr[], returns the
# maximum j – i such that arr[j] > arr[i]
def maxIndexDiff(arr, n):
     
    rightMax = [0] * n
    rightMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], arr[i])
         
    # rightMax[i] = max arr[i...(n-1]
    maxDist = -2**31
    i = 0
    j = 0
     
    while (i < n and j < n):
        if (rightMax[j] >= arr[i]):
            maxDist = max(maxDist, j - i)
            j += 1
             
        else:
             
            # if(rightMax[j] < leftMin[i])
            i += 1
     
    return maxDist
 
# Driver Code
arr = [ 34, 8, 10, 3, 2, 80, 30, 33, 1 ]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
 
print(maxDiff)



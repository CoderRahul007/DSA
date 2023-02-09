# Given two sorted arrays of size m and n respectively, you are tasked with 
# finding the element that would be at the k’th position of the final sorted array.

# Examples: 

# Input : Array 1 - 2 3 6 7 9
#         Array 2 - 1 4 8 10
#         k = 5
# Output : 6
# Explanation: The final sorted array would be -
# 1, 2, 3, 4, 6, 7, 8, 9, 10
# The 5th element of this array is 6.

# Input : Array 1 - 100 112 256 349 770
#         Array 2 - 72 86 113 119 265 445 892
#         k = 7
# Output : 256
# Explanation: Final sorted array is -
# 72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892
# 7th element of this array is 256.

# Python3 Program to find kth element
# from two sorted arrays

def find(A, B, m, n, k_req):
	i, j, k = 0, 0, 0

	# Keep taking smaller of the current
	# elements of two sorted arrays and
	# keep incrementing k
	while i < len(A) and j < len(B):
		if A[i] < B[j]:
			k += 1
			if k == k_req:
				return A[i]
			i += 1
		else:
			k += 1
			if k == k_req:
				return B[j]	
			j += 1

	# If array B[] is completely traversed
	while i < len(A):
		k += 1
		if k == k_req:
				return A[i]
		i += 1


	# If array A[] is completely traversed
	while j < len(B):
		k += 1
		if k == k_req:
				return B[j]
		j += 1

# driver code
A = [2, 3, 6, 7, 9]
B = [1, 4, 8, 10]
k = 5
print(find(A, B, 5, 4, k))
# time complexity of O(k)


# https://takeuforward.org/data-structure/k-th-element-of-two-sorted-arrays/
# https://www.youtube.com/watch?v=l5siJgontlE
# Time Complexity : log(min(m,n))
import sys
def kthelementoptimised(arr1 , arr2 , m , n , k):
    if m > n:
        return kthelementoptimised(arr2, arr1, n, m, k)
    low = max(0 , k-m)
    high = min(k , n)

    while low <= high :
        cut1 = (low + high) >> 1
        cut2 = k - cut1
        l1 = -sys.maxsize  if cut1 == 0  else arr1[cut1 - 1] 
        l2 = -sys.maxsize  if cut2 == 0 else arr2[cut2 - 1]
        r1 = sys.maxsize  if cut1 == n else arr1[cut1]
        r2 =  sys.maxsize if cut2 == m else arr2[cut2] 

        if l1 <= r2 and l2 <= r1:
            return max(l1 , l2)
        elif l1 > r2:
            high = cut1 -1
        else:
            low = cut1 +1
    return -1

import sys
class Solution:
    def kthElement(self,  arr1, arr2, m, n, k):
            
        if m > n:
                return self.kthElement(arr2, arr1, n, m, k)
        low = max(0 , k-m)
        high = min(k , n)
    
        while low <= high :
            cut1 = (low + high) // 2
            cut2 = k - cut1
            print(cut1 , cut2)
            l1 = -sys.maxsize  if cut1 <= 0  else arr1[cut1 - 1] 
            l2 = -sys.maxsize  if cut2 <= 0 else arr2[cut2 - 1]
            r1 = sys.maxsize  if cut1 >= n else arr1[cut1]
            r2 =  sys.maxsize if cut2 >= m else arr2[cut2] 
    
            if l1 <= r2 and l2 <= r1:
                return max(l1 , l2)
            elif l1 > r2:
                high = cut1 -1
            else:
                low = cut1 +1
        return -1
		
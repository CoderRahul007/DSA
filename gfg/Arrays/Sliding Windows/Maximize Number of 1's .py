# Given a binary array arr of size N and an integer M. Find the maximum number of
#  consecutive 1's produced by flipping at most M 0's.
 

# Example 1:

# Input:
# N = 3
# arr[] = {1, 0, 1}
# M = 1
# Output:
# 3
# Explanation:
# Maximum subarray is of size 3
# which can be made subarray of all 1 after
# flipping two zeros to 1.

# Example 2:

# Input:
# N = 11
# arr[] = {1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1}
# M = 2
# Output:
# 8
# Explanation:
# Maximum subarray is of size 8
# which can be made subarray of all 1 after
# flipping two zeros to 1.



def findZeroes(arr, n, m) :
    # code here
    if n == 1 and m <= 1:
        return 1
    left = 0
    maxl = 0
    c = 0
    for right in range(n):
        if arr[right] == 0:
            c +=1
        while c > m and left <= right:
            if arr[left] == 0:
                c-=1
            left+=1
        maxl = max(maxl , right - left +1)
    return maxl
# O(n)
#OR     

def findZeroes(arr, n, m) :
    # code here
    left = 0
    right = 0
    currl = 0
    maxl = 0
    c = 0
    while right < n:
        if arr[right] == 1:
            currl +=1
        else:
            c +=1
            currl +=1
            while c > m:
                if arr[left] == 0:
                    c -=1
                currl -=1
                left+=1
        right +=1
        maxl = max(currl , maxl)
    return maxl


# Given an array A[] of N positive integers which can contain integers from 1 to P
#  where elements can be repeated or can be absent from the array. Your task is to count 
# the frequency of all elements from 1 to N.
# Note: The elements greater than N in the array can be ignored for counting.


# Example 1:

# Input:
# N = 5
# arr[] = {2, 3, 2, 3, 5}
# P = 5
# Output:
# 0 2 2 0 1
# Explanation: 
# Counting frequencies of each array element
# We have:
# 1 occurring 0 times.
# 2 occurring 2 times.
# 3 occurring 2 times.
# 4 occurring 0 times.
# 5 occurring 1 time.

# Example 2:

# Input:
# N = 4
# arr[] = {3,3,3,3}
# P = 3
# Output:
# 0 0 4 0
# Explanation: 
# Counting frequencies of each array element
# We have:
# 1 occurring 0 times.
# 2 occurring 0 times.
# 3 occurring 4 times.
# 4 occurring 0 times.

from collections import Counter

def frequencyCount( arr, N, P):
    t = [0]*(P+1)
    for i in range(N):
        t[arr[i]-1]+=1
    for i in range(N):
        if i<P:
            arr[i] = t[i]
        else:
            arr[i] = 0
            
def frequencyCount( arr, N, P ):

    d = Counter(arr)
    for i in range(1,N+1):
        if i not in d:
            arr[i-1]=0
        else:
            arr[i-1] = d[i]
    return arr
N = 4
arr = [3,3,3,3]
P = 3
print(frequencyCount(arr , N , P))

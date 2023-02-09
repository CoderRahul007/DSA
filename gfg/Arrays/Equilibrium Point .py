# Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.

# Note: Retun the index of Equilibrium point. (1-based index)

# Example 1:

# Input: 
# n = 5 
# A[] = {1,3,5,2,2} 
# Output: 3 
# Explanation: For second test case 
# equilibrium point is at position 3 
# as elements before it (1+3) = 
# elements after it (2+2). 

def equilibriumPoint(A, N):
    # Your code here
    s = sum(A)
    l = 0
    if N == 1:
        return 1
    for i in range(1 ,N):
        l += A[i-1]
        if l == s-l-A[i] :
            return i+1
    return -1
            
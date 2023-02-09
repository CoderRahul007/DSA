def findEquilibrium(a,n):
    # Code here
    s = sum(a)
    lefts = 0
    rights = s
    for i in range(n):
        rights -= a[i]
        if lefts == rights :
            return i
        lefts += a[i]
    return -1


# Equilibrium index of an array is an index such that the sum of elements at lower indexes 
# is equal to the sum of elements at higher indexes.
# Given an array, your task is to find the index of first Equilibrium point in the array.

# Input Format:
# The first line of input takes an integer T denoting the no of test cases, then T test cases follow. 
# The first line of each test case is an integer N denoting The size of the array. Then in the next 
# line are N space-separated values of the array. 

# Output Format:
# For each test case, the output will be the equilibrium index of the array. If no such index 
# exists output will be -1.
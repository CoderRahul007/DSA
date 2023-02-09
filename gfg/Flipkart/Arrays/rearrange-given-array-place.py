# Given an array arr[] of size n where every element is in range from 0 to n-1.
#  Rearrange the given array so that arr[i] becomes arr[arr[i]]. This should be done with O(1) extra space.

# Examples: 

# Input: arr[]  = {3, 2, 0, 1}
# Output: arr[] = {1, 0, 3, 2}
# Explanation: 
# In the given array 
# arr[arr[0]] is 1 so arr[0] in output array is 1
# arr[arr[1]] is 0 so arr[1] in output array is 0
# arr[arr[2]] is 3 so arr[2] in output array is 3
# arr[arr[3]] is 2 so arr[3] in output array is 2

# Input: arr[] = {4, 0, 2, 1, 3}
# Output: arr[] = {3, 4, 2, 0, 1}
# Explanation:
# arr[arr[0]] is 3 so arr[0] in output array is 3
# arr[arr[1]] is 4 so arr[1] in output array is 4
# arr[arr[2]] is 2 so arr[2] in output array is 2
# arr[arr[3]] is 0 so arr[3] in output array is 0
# arr[arr[4]] is 1 so arr[4] in output array is 1

# Input: arr[] = {0, 1, 2, 3}
# Output: arr[] = {0, 1, 2, 3}
# Explanation:
# arr[arr[0]] is 0 so arr[0] in output array is 0
# arr[arr[1]] is 1 so arr[1] in output array is 1
# arr[arr[2]] is 2 so arr[2] in output array is 2
# arr[arr[3]] is 3 so arr[3] in output array is 3


# Approach: The array elements of the given array lies from 0 to n-1. Now an array element is needed
#  that can store two different values at the same time. To achieve this, every element at ith index 
# is incremented by (arr[arr[i]] % n)*n.After the increment operation of first step, every element holds both old values and new values. Old value can be obtained by arr[i]%n and a new value can be obtained by arr[i]/n.

# How this can be achieved? 
# Let’s assume an element is a and another element is b, both the elements are less than n. So if an 
# element a is incremented by b*n. So the element becomes a + b*n so when a + b*n is divided by n then the value is b and a + b*n % n is a.

# Algorithm:  

# Traverse the array from start to end.
# For every index increment the element by array[array[index] ] % n. To get the ith element find the modulo with n, i.e array[index]%n.
# Again Traverse the array from start to end
# Print the ith element after dividing the ith element by n, i.e. array[i]/n.
# Implementation: 
 


# Python3 program to Rearrange
# an array so that arr[i] becomes
# arr[arr[i]]
 
# The function to rearrange an
# array in-place so that arr[i]
# becomes arr[arr[i]].
def rearrange(arr, n):
 
    # First step: Increase all values
    # by (arr[arr[i]] % n) * n
    for i in range(0, n):
        arr[i] += (arr[arr[i]] % n) * n
 
    # Second Step: Divide all values
    # by n
    for i in range(0, n):
        arr[i] = int(arr[i] / n)
 
# A utility function to print
# an array of size n
def printArr(arr, n):
 
    for i in range(0, n):
        print (arr[i], end =" ")
    print ("")
 
# Driver program
arr = [3, 2, 0, 1]
n = len(arr)
 
print ("Given array is")
printArr(arr, n)
 
rearrange(arr, n);
print ("Modified array is")
printArr(arr, n)
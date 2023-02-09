
"""
    Time Complexity: O(N*(2^N))
    Space Complexity: O(N*(2^N))

    Where N is the number of elements in array
"""
from os import *
from sys import *
from collections import *
from math import *

def pwset(v):
    # Write your code here
    # Return a 2-D list containing all subsets
    v.sort()
    ans = []
    n = len(v)
    for i in range(2**n+1):
        tmp = []
        for j in range(n):
            if i & (1 << j):               
                tmp.append(v[j])
        ans.append(tmp[:])
    return ans

# Time Complexity

# O(N*(2^N)), where N is the length of the string.

 

# As we are traversing from 0 to 2^N. Along with this in each iteration also traversing
#  the whole array of size N.So we can say we have a time complexity of O(N*(2^N)).
# Space Complexity

# O(N*(2^N)), where N is the length of the string.

# As we finally generating 2^N arrays and the size of the biggest array is N. Hence, 
# the overall space complexity is O(N*(2^N)).

#######################################################################################3
# Recursion
"""
    Time Complexity: O(2^N)
    Space Complexity: O(N*(2^N))

    Where N is the number of elements in array
"""

def solve(idx, arr, curr, ans):

    # Base condition
    if (idx >= len(arr)):
        ans.append(curr.copy())
        return

    # Recursive Call to not include ARR[idx] in the subset
    solve(idx + 1, arr, curr, ans)

    # Recursive Call to include ARR[idx] in the subset
    curr.append(arr[idx])
    solve(idx + 1, arr, curr, ans)
    
    curr.pop()


def pwset(arr):

    # Create an array to store all subsets
    ans = []

    curr = []
    idx = 0

    solve(idx, arr, curr, ans)

    # Return the array ans
    return ans

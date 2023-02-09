# Problem Statement
# Given an array of integers ‘ARR’ and an integer ‘X’, you are supposed to find the 
# number of subarrays of 'ARR' which have bitwise XOR of the elements equal to 'X'.
# Note:

# An array ‘B’ is a subarray of an array ‘A’ if ‘B’ that can be obtained by deletion of,
#  several elements(possibly none) from the start of ‘A’ and several elements(possibly none) from the end of ‘A’. 

def subarraysXor(arr, x):
    # Write your code here
    # Return an integer
    mp = {}
    n = len(arr)
    c = 0
    xr = 0
    for i in range(n):
        xr =  xr ^ arr[i]
        if xr == x:
            c+=1
        if xr ^ x in mp:
            c+= mp[xr ^ x]
        if xr in mp:
            mp[xr]+=1
        else:
            mp[xr] = 1       
    return c
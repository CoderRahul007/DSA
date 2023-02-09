# Given a sorted array containing only 0s and 1s, find the transition point. 


# Example 1:

# Input:
# N = 5
# arr[] = {0,0,0,1,1}
# Output: 3
# Explanation: index 3 is the transition 
# point where 1 begins.

def transitionPoint(arr, n):

    l = 0
    r = n-1
    while l <= r:
        m = (l + r)>>1
        if arr[m] < 1:
            l = m +1
        else:
            r = m -1
    return -1 if l == n else l  

arr = [0,0,0,1,1]
print(transitionPoint(arr , len(arr)))
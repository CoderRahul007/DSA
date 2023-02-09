def minDist(self, arr, n, x, y):
    xi = -1
    yi = -1
    mini = 9999999999
    for i in range(n):
        if arr[i] == x:
            xi = i
        if arr[i] == y:
            yi = i
        
        if xi != -1 and yi != -1:
            mini = min(mini , abs(xi-yi))
    if xi == -1 or yi == -1:
        
            return -1
    return mini


# You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

# Example 1:

# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are
# two distances between x and y, which are
# 1 and 3 out of which the least is 1.

# Example 2:

# Input:
# N = 7
# A[] = {86,39,90,67,84,66,62}
# x = 42, y = 12
# Output: -1
# Explanation: x = 42 and y = 12. We return
# -1 as x and y don't exist in the array.
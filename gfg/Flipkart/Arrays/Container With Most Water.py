# Given N non-negative integers a1,a2,....an where each represents a point at coordinate (i, ai).
#  N vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i,0). 
# Find two lines, which together with x-axis forms a container, such that it contains the most water.

# Example 1:

# Input:
# N = 4
# a[] = {1,5,4,3}
# Output: 6
# Explanation: 5 and 3 are distance 2 apart.
# So the size of the base = 2. Height of
# container = min(5, 3) = 3. So total area
# = 3 * 2 = 6.

# Example 2:

# Input:
# N = 5
# a[] = {3,1,2,4,5}
# Output: 12
# Explanation: 5 and 3 are distance 4 apart.
# So the size of the base = 4. Height of
# container = min(5, 3) = 3. So total area
# = 4 * 3 = 12.

def maxArea(A,le):
    ans=0
    i=0
    j=len(A)-1
    while i<j:
        temp=(j-i)*min(A[i],A[j])
        ans=max(ans,temp)
        if A[i]<A[j]:
            i+=1
        else:
            j-=1
    return ans
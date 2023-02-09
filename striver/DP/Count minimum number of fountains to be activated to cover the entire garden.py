# There is a one-dimensional garden of length N. In each position of the N length garden,
#  a fountain has been installed. Given an array a[]such that a[i] describes the coverage
#  limit of ith fountain. A fountain can cover the range from the position max(i – a[i], 1) 
# to min(i + a[i], N). In beginning, all the fountains are switched off. The task is to find
#  the minimum number of fountains needed to be activated such that the whole N-length garden can be covered by water.

# Examples:

# Input: a[] = {1, 2, 1}
# Output: 1
# Explanation:
# For position 1: a[1] = 1, range = 1 to 2
# For position 2: a[2] = 2, range = 1 to 3
# For position 3: a[3] = 1, range = 2 to 3
# Therefore, the fountain at position a[2] covers the whole garden.
# Therefore, the required output is 1.

# Input: a[] = {2, 1, 1, 2, 1} 
# Output: 2 

#################################################################################################################
# DP Solution
# https://www.youtube.com/watch?v=zmbSoHiRHX4
def minTaps( arr ):
    dp = [float(inf)] * (n+1)
    dp[0] = 0
    for i in range(n):
        leftReach = max(0 , i - ranges[i])
        for j in range(max(0 , i-range(i) + 1) , min(i + range[i], n) + 1):
            dp[j] = min(dp[j] , dp[leftReach] + 1)
    # the dp[j] will dp[leftreach] + 1 , wherer 1  is the next tap to open
    return -1 if dp[n] == float('inf')  else dp[n]

#################################################################################################################
#Greedy O(n) and O(1)
 
def minCntFoun(a, N):
 
    # dp[i]: Stores the position of
    # rightmost fountain that can
    # be covered by water of leftmost
    # fountain of the i-th fountain
    dp = [0] * N
    for i in range(N):
      dp[i] = -1
 
    # Traverse the array
    for i in range(N):
        idxLeft = max(i - a[i], 0)
        idxRight = min(i + (a[i] + 1), N)
        dp[idxLeft] = max(dp[idxLeft],
                          idxRight)
 
    # Stores count of fountains
    # needed to be activated
    cntfount = 1
 
    idxRight = dp[0]
 
    # Stores index of next fountain
    # that needed to be activated
    idxNext = 0
 
    # Traverse dp[] array
    for i in range(N):
        idxNext = max( idxNext, dp[i] )
 
        # If left most fountain
        # cover all its range
        if (i == idxRight):
            cntfount += 1
            idxRight = idxNext
 
    return cntfount
 
 
# Driver code
if __name__ == '__main__':
 
    a = [1, 2, 1]
    N = len(a)
 
    print(minCntFoun(a, N))

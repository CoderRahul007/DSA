def numberOfPathsRecur(m, n):
# If either given row number is first
# or given column number is first
    if(m == 1 or n == 1):
        return 1
 
# If diagonal movements are allowed
# then the last addition
# is required.
    return numberOfPathsRecur(m-1, n) + numberOfPathsRecur(m, n-1)
    # one row decresase and one columsn decrease

def numberOfPathsDP(m , n):
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return (dp[m-1][n-1])

def numberOfPathsOPtimises(p, q):
     
    # Create a 1D array to store
    # results of subproblems
    dp = [1 for i in range(q)]
    for i in range(p - 1):
        print("i ",i)
        for j in range(1, q):
            print("j ",j)
            print("dp[j-1] ", dp[j-1])
            print("Before dp[j] ", dp[j])
            dp[j] += dp[j - 1]
            print("After dp[j] ", dp[j])
    print(dp)
    return dp[q - 1]
 
# Driver Code
print(numberOfPathsOPtimises(3, 3))

# m and n are dimensions of matrix
m = 3
n = 3
print(numberOfPathsRecur(m, n))
print(numberOfPathsDP(m, n))
# Given a string, find the length of the longest repeating subsequence such that
#  the two subsequences don’t have same string character at the same position, i.e.,
#  any i’th character in the two subsequences shouldn’t have the same index in the original string. 
# Input: str = "abc"
# Output: 0
# There is no repeating subsequence
# it means i dont have to use the same index for calculating the next subsequence


# Input: str = "aab"
# Output: 1
# The two subsequence are 'a'(first) and 'a'(second). 
# Note that 'A' cannot be considered as part of subsequence 
# as it would be at same index in both.

# Input: str = "aabb"
# Output: 2

# Input: str = "axxxy"
# Output: 2

def LRS(A ):
    m = len(A)    
    dp = [[0] * (m+1) for j in range(m+1)]

    for i in range(m+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif A[i-1] == A[j-1] and i != j:# here i!=j is imp
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
    return dp[m][m]

print(LRS("aabb"))
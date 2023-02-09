# iven two strings X and Y, and two values costX and costY.
#  We need to find minimum cost required to make the given two strings identical.
#  We can delete characters from both the strings. The cost of deleting a character from string X is costX and from Y is costY. Cost of removing all characters from a string is same. 

# Examples : 

# Input :  X = "abcd", Y = "acdb", costX = 10, costY = 20.
# Output:  30
# For Making both strings identical we have to delete 
# character 'b' from both the string, hence cost will
# be = 10 + 20 = 30.

# Input :  X = "ef", Y = "gh", costX = 10, costY = 20.
# Output:  60
# For making both strings identical, we have to delete 2-2
# characters from both the strings, hence cost will be =
#  10 + 10 + 20 + 20 = 60.
# Recommended Practice
# Minimum Cost To Make Two Strings Identical
# Try It!

# This problem is a variation of Longest Common Subsequence ( LCS ).
#  The idea is simple, we first find the length of longest common
#  subsequence of strings X and Y. Now subtracting len_LCS with lengths 
# of individual strings gives us number of characters to be removed to make them identical.  

# // Cost of making two strings identical is SUM of following two
# //   1) Cost of removing extra characters (other than LCS) 
# //      from X[]
# //   2) Cost of removing extra characters (other than LCS) 
# //      from Y[]
# Minimum Cost to make strings identical = costX * (m - len_LCS) + 
#                                          costY * (n - len_LCS).  

# m ==> Length of string X
# m ==> Length of string Y
# len_LCS ==> Length of LCS Of X and Y.
# costX ==> Cost of removing a character from X[]
# costY ==> Cost of removing a character from Y[]

# Note that cost of removing all characters from a string
# is same.               
# Below is the implementation of above idea. 



 
# Returns length of LCS for
# X[0..m-1], Y[0..n-1]
def lcs(X, Y, m, n):
    L = [[0 for i in range(n + 1)]
            for i in range(m + 1)]
             
    # Following steps build
    # L[m+1][n+1] in bottom
    # up fashion. Note that
    # L[i][j] contains length
    # of LCS of X[0..i-1] and Y[0..j-1]
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
        # L[m][n] contains length of
        # LCS for X[0..n-1] and Y[0..m-1]
    return L[m][n]
     
# Returns cost of making X[]
# and Y[] identical. costX is
# cost of removing a character
# from X[] and costY is cost
# of removing a character from Y[]
def findMinCost(X, Y, costX, costY):
     
    # Find LCS of X[] and Y[]
    m = len(X)
    n = len(Y)
    len_LCS =lcs(X, Y, m, n)
     
    # Cost of making two strings
    # identical is SUM of following two
    # 1) Cost of removing extra 
    # characters from first string
    # 2) Cost of removing extra
    # characters from second string
    return (costX * (m - len_LCS) +
            costY * (n - len_LCS))
             
# Driver Code
X = "ef"
Y = "gh"
print('Minimum Cost to make two strings ', end = '')
print('identical is = ', findMinCost(X, Y, 10, 20))
 

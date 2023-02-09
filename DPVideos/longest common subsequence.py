def lcs(A , B , a1 , b1):
    if a1 == 0 or b1 == 0 :
        return 0
    if A[a1 -1] == B[b1 -1]:
        return 1 + lcs(A , B , a1-1 , b1 -1)   # it means u have recursed to  both A and B  previos matching items
    else:
        return max(lcs(A , B , a1-1 , b1) ,  lcs(A , B , a1 , b1-1))
        #it means u have recursed to max of first A and then B  previos matching items


def printLCS(dp , A , B , a1 , b1):
    if a1 == 0 or b1 == 0:
        return ""
    if A[a1] == B[b1]:
        return A[a1] + printLCS(dp , A , B , a1-1 , b1 -1)   # it means u have recursed to  both A and B  previos matching items
    if dp[a1][b1-1] > dp[a1-1][b1]:
        return   printLCS(A , B , a1 , b1-1)
    return  printLCS(A , B , a1-1 , b1)



def lcsDP(X , Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)
 
    # declaring the array for storing the dp values
    L = [[None]*(n+1) for i in range(m+1)]
 
    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j] , L[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    print(L[m][n])
    print(L)

    lcs = ""
 
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    while i > 0 and j > 0:
 
        # If current character in X[] and Y are same, then
        # current character is part of LCS
        if X[i-1] == Y[j-1]:
            lcs += X[i-1]
            i -= 1
            j -= 1
 
        # If not same, then find the larger of two and
        # go in the direction of larger value
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
             
        else:
            j -= 1
 
    # We traversed the table in reverse order
    # LCS is the reverse of what we got
    lcs = lcs[::-1]
    print("LCS of " + X + " and " + Y + " is " + lcs)
 


# X = "AGGTAB"
# Y = "GXTXAYB"
# X = "algorithm"
# Y = "rhythm"
X = "aab"
Y = "abbabb"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )
lcsDP(X , Y)
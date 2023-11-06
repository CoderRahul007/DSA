def patternMatching(a , b):
    m = len(a)
    n = len(b)

    dp = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j == 0:
                dp[i][j]= 0
            elif a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max( dp[i-1][j] , dp[i][j-1])
    print(dp[m][n])
    lcs = ""

    i = m
    j = n
    while i > 0 and j > 0:
        
        if a[i-1] == b[j-1]:
            lcs += a[i-1]
            i -= 1
            j -= 1
      
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
             
        else:
            j -= 1
 
    if "".join(lcs[::-1]) == a:
        print("Pattern Exist")
    else:
        print("No Pattern Exist")



   

a= "aab"
b = "abbabb"
patternMatching(a , b)
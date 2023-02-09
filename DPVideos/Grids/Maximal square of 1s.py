def maximalSquare( mat ):
    row = len(mat)
    col = len(mat[0])

    dp = [[0]*(col+1) for _ in range(row+1)]

    largest = 0

    for i in range(1 , row + 1) :
        for j in range(1 , col +1):
            if mat[i-1][j-1] == 1:
                dp[i][j] = 1 + min(dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1])
                largest = largest if largest > dp[i][j] else dp[i][j]
    print(largest * largest)

M = [[0, 1, 1, 0, 1],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]]
maximalSquare(M)
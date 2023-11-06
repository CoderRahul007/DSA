def rodCuttingRecur(piece , profit , i , target):
    if i < 0 or target == 0:
        return 0
    if piece[i] > target:
        return rodCuttingRecur(piece , profit , i-1 , target)
    else:
        return max(rodCuttingRecur(piece , profit, i-1,target) , profit[i] + rodCuttingRecur(piece , profit , i , target-piece[i]))

def rodCuttingDP(piece , profit , target , n):
    dp = [[0 for i in range(target+1)] for t in range(n+1)]
    
    for i in range(1 , n+1):
        for t in range(1 , target +1):
            if piece[i-1] > t:
                dp[i][t] = dp[i-1][t]
            else:
                dp[i][t] = max(dp[i-1][t] , profit[i-1] + dp[i][t-piece[i-1]])
    return dp[n][target]
    

    
piece = [ 1, 2 ,3 ,4]
profit = [1 , 5 , 8 , 9]
originalLength = 4

print(rodCuttingRecur(piece , profit , len(piece) -1 , originalLength))
print(rodCuttingDP(piece , profit , originalLength , len(piece) -1))


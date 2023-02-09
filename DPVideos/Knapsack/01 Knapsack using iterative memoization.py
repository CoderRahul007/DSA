#    0  1   2   3   4   5   6   

# 0  0   0   0   0   0   0  0

# 1  0  10  10  10  10  10  10

# 2  0  10  15  25  25  25  25

# 3  0  10  15  40  50  55  65

# weights are in column  , items in rows



# i -> Item index
# w -> weight space available


def knapsack(wt , p , W ):
    N = len(wt)
    dp = [[-1 for i in range(W+1)] for j in range(N+1)]

    for i in range(N+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w]=0       # base case of recursion 
            elif wt[i-1] > w:   # i-1 bcz we are using 0 based index for wt array and i= 0 will be 0 and i = 1 will point to first index of wt
                dp[i][w] = dp[i-1][w] # we wont include this item into our solution so using the previous solution of wt array item and we havent decreased the weight
            else:
                dp[i][w] = max(dp[i-1][w] , p[i-1] + dp[i-1][w-wt[i-1]])
                
                # here dp[i-1][w] mean skip the item , p[i-1] means adding the profit of current item , dp[i-1][w-wt[i-1]] include this item and decreese the space available
    return dp[N][W]
    
def knapSackWithOnSpace(W, wt, val, n):
    dp = [0 for i in range(W+1)]  # Making the dp array
  
    for i in range(1, n+1):  # taking first i elements
        for w in range(W, 0, -1):  # starting from back,so that we also have data of
                                # previous computation when taking i-1 items
            if wt[i-1] <= w:
                # finding the maximum value
                dp[w] = max(dp[w], dp[w-wt[i-1]]+val[i-1])
  
    return dp[W]  #
wt = [3,2,4]
p = [6,8,7]
space = 8
print(knapsack(wt,p,space))
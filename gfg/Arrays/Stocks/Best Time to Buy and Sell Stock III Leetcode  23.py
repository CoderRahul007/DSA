# https://www.youtube.com/watch?v=37s1_xBiqH0

# At most 2 transaction return the max profit on buy and sell

def memoization(prices, pos, t, bought , mem ):
    '''           
        pos->current position
        t->transactions done
        bought->If current stock is bought
    '''
    if pos >= len(prices) or t == 0: # out of bounds
        return 0
    if mem[bought][t][pos] != -1:
        return mem[bought][t][pos]

    # 3 choices for a position-->Buy/Sell/Skip        
    res = memoization(prices , pos+1 , t , bought , mem)
    if bought :
        res = max(res , memoization(prices , pos+1 , t-1 , False) + prices[pos] , mem) # sell
    else:
        res = max(res , memoization(prices , pos+1 , t , True) - prices[pos] , mem) # buy
    mem[bought][t][pos] = res
    return res

def callmemo():
    prices = []
    mem = [[[-1 for i in range(2)] for j in range(3)] for k in range(len(prices))]
    res = memoization(prices , 0 , 2 , False,  mem)
    return res


def maxProfitStock( prices ):
    n = len(prices)
    if n==0:
        return 0
    left = [0]*n
    right = [0]*n
    leftmin = prices[0]

    for i in range(1 , n):
        left[i] = max(left[i-1] , prices[i] -  leftmin)
        leftmin = min(leftmin , prices[i])
    
    rightMax = prices[n-1]

    for j in range(n-2 , -1 , -1):
        right[i] = max(right[i+1] , rightMax - prices[i])
        rightMax = max(rightMax  , prices[i])

    profit = right[0]
    for i in range(1  , n):
        profit = max( profit , left[i-1] + right[i])
    return profit


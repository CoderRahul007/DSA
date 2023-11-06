##### Using Recursion  ####

# https://www.youtube.com/watch?v=mGfK-j9gAQA&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=4

# prints maximum profit

def knapsack(wt, p, space, i):
    if i < 0 or space == 0:
        return 0
    if wt[i] > space:  # exclude the item
        return knapsack(wt, p, space, i-1)
    else:  # include the item

        exclude = knapsack(wt, p, space, i-1)
        include = p[i] + knapsack(wt, p, space - wt[i], i-1)

        return max(exclude, include)
        # max of  exclude or include to find the max profit

# O(2^N) every combinations find


wt = [3, 2, 4]
profit = [6, 8, 7]
space = 8
i = len(wt)-1
print(knapsack(wt, profit, space, i))

# we are going from right to left of weight array


############# Using Memoization #############


# Stack memory is close to 1 MB and heap is 256 MB
# in recurisve call stack overflow may happen

def knapsack(wt, p, space, i, mem):
    if i < 0 or space == 0:
        return 0
    if mem[i][space] != -1:
        return mem[i][space]
    if wt[i] > space:  # exclude the item
        # means to get the prev value since i is not included here
        mem[i][space] = knapsack(wt, p, space, i-1, mem)

    else:  # include the item
        exclude = knapsack(wt, p, space, i-1, mem)
        include = p[i] + knapsack(wt, p, space - wt[i], i-1, mem)

        mem[i][space] = max(exclude, include)
        # max of exclude or include to find the max profit

    return mem[i][space]

    # here i means when i has been 0 and space is 8 then what is the max prodit is returned


# O(W*N) table size time and space complexity

wt = [3, 2, 4]
p = [6, 8, 7]
space = 8
i = len(wt)-1
mem = [[-1 for j in range((space + 1))] for i in range(len(p)+1)]
print(knapsack(wt, p, space, i, mem))

# https://www.youtube.com/watch?v=dT6dvdbpChA&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=5

################################## Using Iterative Memoization ####

#    0  1   2   3   4   5   6   --- weights

# 0  0   0   0   0   0   0  0

# 1  0  10  10  10  10  10  10

# 2  0  10  15  25  25  25  25

# 3  0  10  15  40  50  55  65

# |
# items

# weights are in column  , items in rows


# i -> Item index
# w -> weight space available


def knapsack(wt, p, W):
    N = len(wt)
    dp = [[-1 for j in range(W+1)] for i in range(N+1)]

    # we will start from the first element and check if only 1st element is taken into consideration then what is max profit for each weight
    for i in range(N+1):
        for w in range(W+1):

            curr_ele_index = i-1
            
            if i == 0 or w == 0:
                dp[i][w] = 0
                # base case of recursion            
            elif wt[curr_ele_index] > w:
                # i-1 bcz we are using 0 based index for wt array and i= 0 will be 0 and i = 1 will point to first index of wt
                # we wont include this item into our solution so using the previous solution of wt array item and we havent decreased the weight
                dp[i][w] = dp[curr_ele_index][w]
            else:
                dp[i][w] = max(dp[curr_ele_index][w], p[curr_ele_index] + dp[curr_ele_index][w-wt[curr_ele_index]])

                # here dp[curr_ele_index][w] mean skip the item , p[curr_ele_index] means adding the profit of current item , dp[curr_ele_index][w-wt[curr_ele_index]] include this item and decreese the space available
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


wt = [3, 2, 4]
p = [6, 8, 7]
space = 8
print(knapsack(wt, p, space))

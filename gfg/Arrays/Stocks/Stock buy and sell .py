# The cost of stock on each day is given in an array A[] of size N. 
# Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

# Example 1:

# Input:
# N = 7
# A[] = { 100, 180, 260, 310, 40, 535, 695 }

# Output:
# (0 3) (4 6)

# Explanation 1:
# We can buy stock on day 0, 
# and sell it on 3rd day, 
# which will give us maximum profit.

# Example 2:

# Input:
# N = 10
# A[] = {23, 13, 25, 29, 33, 19, 34, 45, 65, 67}

# Output:
# (1 4) (5 9)

# Obviously, we need to sell when the prices are highest, and buy when prices are lowest.

# But how to determine, that the prices are highest and lowest.

# The Local Minima are the points of Lowest price and Local Maxima are the points of Highest price.

# Iterate through the complete array, and store these points of Local Minima and then store these points of Local Maxima.

def stockBuySell(price, n):
    # code here
    i = 0
    while i+1 < n and price[i] > price[i+1]:
        i+=1
    if i == n-1:
        print("No Profit")
    
    while i < n:
        j = i
        while i+1 < n and price[i] < price[i+1]:
            i+=1
        if j != i:
            print("(",j,i,")" , end = " ")
        i+=1
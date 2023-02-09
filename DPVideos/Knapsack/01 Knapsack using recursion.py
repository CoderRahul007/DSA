# https://www.youtube.com/watch?v=mGfK-j9gAQA&list=PLEJXowNB4kPxBwaXtRO1qFLpCzF75DYrS&index=4

#prints maximum profit

def knapsack(wt , p , space , i):
    if i < 0 or space == 0:
        return 0
    if wt[i] > space:       #exclude the item
        return knapsack(wt , p , space , i-1)
    else:   #include the item
        return max( knapsack(wt , p , space , i-1) ,
         p[i] + knapsack(wt , p , space - wt[i] , i-1))
        # exclude or include to find the max profit

# O(2^N) every combinations find

wt = [3,2,4]
p = [6,8,7]
space = 8
i = len(wt)-1
print(knapsack(wt,p,space,i))

# we are going from left to right of weight array
# Problem Statement
# You have been given weights and values of ‘N’ items. You are also given a knapsack of size ‘W’.
# Your task is to put the items in the knapsack such that the total value of items in the knapsack is maximum.
# Note:

# You are allowed to break the items.


'''
    Time Complexity : O(N * log(N))
    Space Complexity : O(1)

    where N is the number of items.
'''


# Comparator to sort items.
def compare(a):
    
    return a[1] / a[0]


def maximumValue(items, n, w):

    # Sort items according to value/weight.
    items = sorted(items, key = compare, reverse = True)  # descending order 0 -> weight , 1 -> value

    maxValue = 0
    currWeight = 0

    for i in range(n):
        if currWeight + items[i][0] <= w:
            currWeight += items[i][0]
            maxValue += items[i][1]

        else:
            remainingWeight = w - currWeight

            # Pick a fraction of current item.
            maxValue += items[i][1] * (remainingWeight / items[i][0]) # (rem/wt)*val
            break

    return round(maxValue, 2)
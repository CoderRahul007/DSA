# arr = [1,3,5,9]
# then arr1 = [1,3,5] and arr2 = [9]
# Intuition sum of array should be even and check for 0 1 knapsack for sum/2

def equalPartitionExist(set):
    # The value of subset[i][j] will be true if there is a 
    # subset of set[0..j-1] with sum equal to i 
    n = len(set)
    sum = 0
    for i in set:
        sum += i

    if sum & 1:  # if odd
        return False

    subset = [[-1 for i in range(sum//2 + 1)] for j in range(n + 1)]
    for i in range(n + 1):  # If sum is 0, then answer is true , this is row
        subset[i][0] = True
    for i in range(1 ,sum //2+ 1): # If sum is not 0 and set is empty, then answer is false , this is column
        subset[0][i] = False
    
    for i in range(1, n + 1):
        for j in range(1, sum//2 + 1):
            if j < set[i-1]:  # if less then dont include
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]: # both option exclude and include
                subset[i][j] = subset[i-1][j] or subset[i-1][j-set[i-1]]
    return subset[n][sum//2]  


arr = [1,3,5]
print(equalPartitionExist(arr))
# arr = [1,3,5,9]
# then arr1 = [1,3,5] and arr2 = [9]
# Intuition total of array should be even and check for 0 1 knapsack for total/2

def equalPartitionExist(arr):
    # The value of subset[i][j] will be true if there is a 
    # subset of arr[0..j-1] with total equal to i 
    n = len(arr)
    total = sum(arr)

    if total & 1:  # if odd
        return False

    subset = [[-1 for i in range(total//2 + 1)] for j in range(n + 1)]
    for i in range(n + 1):  # If total is 0, then answer is true , this is row
        subset[i][0] = True
    for i in range(1 ,total //2+ 1): # If total is not 0 and arr is empty, then answer is false , this is column
        subset[0][i] = False
    
    for i in range(1, n + 1):
        for j in range(1, total//2 + 1):
            if j < arr[i-1]:  # if less then dont include
                subset[i][j] = subset[i-1][j]
            if j >= arr[i-1]: # both option exclude and include
                subset[i][j] = subset[i-1][j] or subset[i-1][j-arr[i-1]]
    return subset[n][total//2]  


arr = [1,3,5]
print(equalPartitionExist(arr))
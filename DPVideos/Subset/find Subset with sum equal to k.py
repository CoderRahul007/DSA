
def hasSubset(set , n , sum):
        if sum == 0:
            return True
        if n == 0 and sum != 0:
            return False
        if set[n-1] > sum:  #If last element is greater than sum, then ignore it 
            return hasSubset(set , n-1 , sum)
        #(a) including the last element
        #(b) excluding the last element
        return hasSubset(set, n-1, sum) or hasSubset(set, n-1, sum-set[n-1])

def hasSubsetUsingMemoizations(set , n , pos, sum , mem) :   
    if sum == 0:
        return True
    if pos >= n or sum < 0:
        return False
    if mem[pos][sum]  != -1:
        return mem[pos][sum]
    
    mem[pos][sum] = hasSubsetUsingMemoizations(set , n , pos +1 , sum-set[pos] , mem) or hasSubsetUsingMemoizations(set , n , pos +1 , sum , mem)
    return mem[pos][sum]
            

def hasSubsetDP(set , n , sum):
    # The value of subset[i][j] will be true if there is a 
    # subset of set[0..j-1] with sum equal to i 

    subset = [[-1 for i in range(sum + 1)] for j in range(n + 1)]
    for i in range(n + 1):  # If sum is 0, then answer is true , this is row
        subset[i][0] = True
    for i in range(1 ,sum + 1): # If sum is not 0 and set is empty, then answer is false , this is column
        subset[0][i] = False
    
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:  # if less then dont include
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]: # both option exclude and include
                subset[i][j] = subset[i-1][j] or subset[i-1][j-set[i-1]]
    return subset[n][sum]   

set = [3, 34, 4, 12, 5, 2]
sum = 13
n = len(set)
mem = [[-1 for i in range(sum+1)] for j in range(n+1)]

print(hasSubset(set , n , sum))
print(hasSubsetDP(set , n , sum))
print(hasSubsetUsingMemoizations(set , n , 0, sum, mem))


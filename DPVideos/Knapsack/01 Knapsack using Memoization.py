# Stack memory is close to 1 MB and heap is 256 MB 
# in recurisve call stack overflow may happen

def knapsack(wt , p , space , i , mem):   
    if i < 0 or space == 0:
        return 0
    if mem[i][space] != -1  :
        return mem[i][space]   
    if wt[i] > space:       #exclude the item
        mem[i][space] =  knapsack(wt , p , space , i-1 , mem )
        
    else:   #include the item
        mem[i][space] = max( knapsack(wt , p , space , i-1 , mem) ,
         p[i] + knapsack(wt , p , space - wt[i] , i-1, mem))
        # exclude or include to find the max profit        
    
    return mem[i][space]


# O(W*N) table size time and space complexity

wt = [3,2,4]
p = [6,8,7]
space = 8
i = len(wt)-1
mem = [[-1 for i in range((space+1))] for j in range(len(p)+1)]
print(knapsack(wt,p,space,i,mem))
def calculateMinPatforms(at, dt, n):
    # Write your code here.
    at.sort()
    dt.sort()
    # check if arrival time of next element is less than departure of previous ele then plat needed is +1

    plat_needed = 1
    res = 1
    i = 1
    j = 0
    while i < n and j < n:
        if at[i] <= dt[j]:
            plat_needed +=1
            i+=1 # increase arrival ele
        elif at[i] > dt[j]:
            plat_needed -=1
            j+=1 # increase departure ele
        res = max( res , plat_needed)        
    return res
# O n logn
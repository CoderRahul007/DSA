def greatestLeast(arr,x):
    l=0
    r=len(arr)-1
    while (r-l)>1:
        m=l+(r-l)//2
        if arr[m]>=x:
            r=m
        else:
            l=m+1 # to converge the search space into l and r at the end whose difference is 1
            # As if element is less than mid then push the search space into greatst element less than X
    if arr[l]==x and l!=0:
        return arr[l-1]
    elif arr[l]!=x:
        return arr[l]
    else:
        return -1
def leastGreatest(arr,x):
    l=0
    r=len(arr)-1
    while (r-l)>1:
        m=l+(r-l)//2
        if arr[m]<=x:
            l=m
        else:
            r=m-1
    if arr[r]==x and r!=len(arr)-1:
        return arr[r+1]
    elif arr[r]!=x:
        return arr[r]
    else:
        return -1
print(greatestLeast([1,1,2,2,2,3,3,4,5],2))
print(leastGreatest([1,1,2,2,2,3,3,4,5],2))
print(greatestLeast([1,1,1,1,1],1))
print(leastGreatest([1,1,1,1,1],1))
print(greatestLeast([1,2,3,4],4))
print(leastGreatest([1,2,3,4],4))

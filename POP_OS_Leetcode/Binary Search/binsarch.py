import functools
import operator
def search(arr,x):
    l=0
    r=len(arr)-1
    while l<r:
        m=(l+r)//2
        if arr[m]>=x:
            r=m
        else:
            l=m+1
    return l
print(search([1,2,3,4],3))
print(search([1,1,1,1,2,3,4],1))
print(functools.reduce(operator.iconcat, [[1,2],[3,4]], []))
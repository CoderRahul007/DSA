# [1,1,2,2,2,3,4,5]
import time
from functools import wraps
def fn_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        t0=time.time()
        result=function(*args,**kwargs)
        t1=time.time()
        print('Total time running %s :%s second' %(function.func_name,str(t1-t0)))
        return result
    return function_timer

@fn_timer
def leftsearch(arr,x):
    l=0
    r=len(arr)-1
    while (r-l)>1:
        m=l+(r-l)//2
        if arr[m]>=x:
            r=m
        else:
            l=m+1
    if arr[l]==x:
        return l
    elif arr[r]==x:
        return r
    else:
        return -1
@fn_timer
def rightsearch(arr,x):
    l=0
    r=len(arr)-1
    while (r-l)>1:
        m=l+(r-l)//2
        if arr[m]<=x:
            l=m
        else:
            r=m-1
    if arr[r]==x:
        return r
    elif arr[l]==x:
        return l
    else:
        return -1
print(leftsearch([1,1,2,2,2,3,3,4,5],2))
print(rightsearch([1,1,2,2,2,3,3,4,5],2))
print(leftsearch([1,1,1,1,1],1))
print(rightsearch([1,1,1,1,1],1))
print(leftsearch([1,2,3,4],4))
print(rightsearch([1,2,3,4],4))

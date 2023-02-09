# Problem Statement
# You are given an array/list say ‘ARR’ of size ‘N’. We call pair (i, j) a 
# Reverse Pair when i < j and 'ARR[i]' > 2 * 'ARR[j]'.
# Your task is to find the number of Reverse Pairs present in given 'ARR'.
# For example :

# For the array [50, 21, 9], if we follow 1-based indexing, the Reverse Pairs
#  are (1, 2), (1, 3) and (2, 3). Thus, the total count i.e. the answer becomes 3.

# Note :

# A single index of the pair (i, j) can be used multiple times.

# just like find inversin
# https://takeuforward.org/data-structure/count-reverse-pairs/
from os import *
from sys import *
from collections import *
from math import *

def merge(arr , low , mid , high):
    c = 0
    j = mid+1
    i = low
    # we have to this before the  merging of left and right subarray bcz we have to find i < j and 'ARR[i]' > 2 * 'ARR[j]'.
    #  after merging it will be lost
    for i in range(low  , mid+1):
        while j <= high and arr[i] > (2 * arr[j]):
            j+=1            
        c+= (j-(mid+1)) # how far j is from the starting of [mid+1 , high] will add to the count since left and rght subarray are sorted
        
    temp = []
    left = low 
    right = mid+1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left +=1
        else:
            temp.append(arr[right])
            right +=1

    while left <= mid:
        temp.append(arr[left])
        left +=1

    while right <= high:
        temp.append(arr[right])
        right +=1

    for i in range(low , high+1):
        arr[i]= temp[i-low]
    return c
        
    
    
    
    
def mergesort(arr , low  , high):
    if low >= high :
        return 0
    mid = (low + high) //2
    c = 0
    c += mergesort(arr , low , mid)
    c+= mergesort(arr , mid+1 , high)
    c+= merge(arr , low  , mid , high)
    return c
        
def reversePairs(arr, n):
    # Write your code here.
    return mergesort(arr , 0 , n-1)


# Output: The Total Reverse Pairs are 2

# Time Complexity : O( N log N ) + O (N) + O (N)   

# Reason : O(N) – Merge operation , O(N) – counting operation 
# ( at each iteration of i , j doesn’t start from 0 . Both of them move linearly ) 

# Space Complexity : O(N) 

# Reason : O(N) – Temporary ArrayList
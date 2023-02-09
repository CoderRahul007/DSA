# Problem Statement
# You are given an array/list 'ARR' of ‘N’ integers and an integer value ‘TARGET’. 
# You need to check whether there exist four numbers (ARR[i], ARR[j], ARR[k], ARR[l])
#  such that (0 <= i < j < k < l < N) and ARR[i] + ARR[j] + ARR[k] + ARR[l] = 'TARGET'.
# Note:

# 1. All four numbers should exist at different indices in the given array.
# 2. The answer is case-sensitive.

def fourSum(arr, target):
    # Write your code here
    arr.sort()
    n = len(arr)
    for i in range(n):
        j = n-1
        while j > i:
            p = target  - arr[i] - arr[j]
            left = i+1
            right = j-1
            while left < right:
                     if p == arr[left] + arr[right]:
                            return "Yes"
                     else:
                        if arr[left] + arr[right] > p:
                            right -=1
                        else:
                            left+=1                                        
            j-=1
    return "No"     

# O(n^3)


def fourSum(arr, target):
    # Write your code here
    n = len(arr)
    mp = {} 
    for i in range(n):
        for j in range(i+1 , n):
            s = arr[i] + arr[j]
            mp[s] = [i , j]
    for i in range(n-1):
        for j in range(i+1 , n):
            left = target - (arr[i] + arr[j])
            if left in mp:
                it = mp[left]
                k  , l = it
                if i != k and i != l and j != k and  j != l:
                    return "Yes"
    return "No"

# O(n^2)
# space - O(n)
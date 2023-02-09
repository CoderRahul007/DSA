# Given an array nums[] of size n, construct a Product Array P (of same size n) 
# such that P[i] is equal to the product of all the elements of nums except nums[i].

 

# Example 1:

# Input:
# n = 5
# nums[] = {10, 3, 5, 6, 2}
# Output:
# 180 600 360 300 900
# Explanation: 
# For i=0, P[i] = 3*5*6*2 = 180.
# For i=1, P[i] = 10*5*6*2 = 600.
# For i=2, P[i] = 10*3*6*2 = 360.
# For i=3, P[i] = 10*3*5*2 = 300.
# For i=4, P[i] = 10*3*5*6 = 900.

# Example 2:

# Input:
# n = 2
# nums[] = {12,0}
# Output:
# 0 12


def productExceptSelf( nums, n):
    #code here
    zeros = 0
    mul = 1
    for i in nums:
        if i == 0:
            zeros +=1
        else:
            mul *= i
    if zeros > 1:
        return [0]*n

    P=[0]*n
    for i, v in enumerate(nums):
        if zeros > 0:
            if v != 0:
                P[i] = 0
            else:
                P[i] = mul
        else:
            P[i] = mul//v
    return P

# Intution if more than 1 is 0 than every element will be 0 else only 0th index element will be mul

def productExceptSelfSpaceN( nums, n):
    #code here
    left = [0]*n
    right  = [0]*n
    left[0] = 1
    right[n-1] = 1
    
    prevleft = nums[0]
    for i in range(1 , n):
        left[i] = prevleft*left[i-1]
        prevleft = nums[i]
    
    rightafter = nums[n-1]
    
    for i in range(n-2 , -1 , -1):
        right[i] = rightafter * right[i+1]
        rightafter = nums[i]
        
    for i in range(n):
        right[i] = right[i]*left[i]
    return right


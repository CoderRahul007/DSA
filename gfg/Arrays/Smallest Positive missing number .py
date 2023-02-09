# You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.

# Example 1:

# Input:
# N = 5
# arr[] = {1,2,3,4,5}
# Output: 6
# Explanation: Smallest positive missing 
# number is 6.

# Example 2:

# Input:
# N = 5
# arr[] = {0,-10,1,3,-20}
# Output: 2
# Explanation: Smallest positive missing 
# number is 2.

# https://www.geeksforgeeks.org/find-the-smallest-positive-number-missing-from-an-unsorted-array/

# Intuition: As we have to calculate the first missing positive integer,and the smallest positive integer is 1.

# So, take ans=1 and iterate over the array once and check whether nums[i]==ans (means we are checking for value from 1 upto missing number).

# By iterating if that condition meet where nums[i]==ans then increment ans by 1 and again check for the same condition uptill size of the array.

# After one scan of array we got the missing number stored in ans variable.

# Now return that ans to the function as return type in int.

def missingNumber(self,arr,n):
    #Your code here
    arr.sort()
    min = 1
    for i in range(n):
        if arr[i] == min:
            min +=1
    return min



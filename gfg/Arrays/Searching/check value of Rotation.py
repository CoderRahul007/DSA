# Given an ascending sorted rotated array Arr of distinct integers of size N.
# The array is right rotated K times. Find the value of K.

# Example 1:

# Input:
# N = 5
# Arr[] = {5, 1, 2, 3, 4}
# Output: 1
# Explanation: The given array is 5 1 2 3 4. 
# The original sorted array is 1 2 3 4 5. 
# We can see that the array was rotated 
# 1 times to the right.

# Example 2:

# Input:
# N = 5
# Arr[] = {1, 2, 3, 4, 5}
# Output: 0
# Explanation: The given array is not rotated.

def findKRotation(arr,  n):
    # code here
    ans = 0
    for i in range(n-1 , 0  , -1): # check from behind if any starting elemtn is greater than next element 
        if arr[i-1] > arr[i]:
            ans=i
            break
    return ans

def bin_search(arr , n):     
        left =  0
        right = n-1
        while left <= right:
            mid =(left+right)//2
            prev = n-1 if mid == 0 else mid -1 # or (m -1 + n) % n
            next = 0 if mid == n-1 else mid +1 # or  ( m + 1) % n
            
            if((arr[mid]<=arr[next] and arr[mid]<=arr[prev])):
              return mid
            elif (arr[mid] > arr[right]):
                left = mid + 1
            else:
                right = mid - 1
            
        
        return 0 
    
arr = [5 , 1 , 2 ,3 , 4]
n = 5
print(bin_search(arr , n))

# Index of smallest element is the count if rotation

# The minimum element is the only element whose previous is greater than it. 
# If there is no previous element, then there is no rotation (first element is minimum).
#  We check this condition for middle element by comparing it with (mid-1)’th and (mid+1)’th elements.
# If the minimum element is not at the middle (neither mid nor mid + 1), then minimum element lies in
#  either left half or right half. 
# If middle element is smaller than last element, then the minimum element lies in left half
# Else minimum element lies in right half.

# Given an array of size N consisting of only 0's and 1's. 
# The array is sorted in such a manner that all the 1's are 
# placed first and then they are followed by all the 0's. Find the count of all the 0's.

# Example 1:

# Input:
# N = 12
# Arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0}
# Output: 3
# Explanation: There are 3 0's in the given array.


# Example 2:

# Input:
# N = 5
# Arr[] = {0, 0, 0, 0, 0}
# Output: 5
# Explanation: There are 5 0's in the array.

def countZerosBinSearch( arr , n ):
    left = 0
    right = n-1
        
    while(left <= right):
            mid = left + (right - left)//2
            print("mid " , mid , "arr[i]" , arr[mid])
            
            if(arr[mid] == 0):
                if(mid == 0 or arr[mid-1] != arr[mid] ):
                    return n-mid
                else:
                    right = mid - 1
            
            else:
                left = mid + 1
        
    return 0

N = 12
arr = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
print(countZerosBinSearch(arr , N))
    
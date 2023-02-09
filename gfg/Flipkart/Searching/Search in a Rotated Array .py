# Basic Solution: 

# Approach: 

# The idea is to find the pivot point, divide the array into two sub-arrays and perform a binary search.
# The main idea for finding a pivot is – for a sorted (in increasing order) and pivoted array,
#  the pivot element is the only element for which the next element to it is smaller than it.
# Using the above statement and binary search pivot can be found.
# After the pivot is found divide the array into two sub-arrays.
# Now the individual sub-arrays are sorted so the element can be searched using Binary Search.
# Implementation:  

# Input arr[] = {3, 4, 5, 1, 2}
# Element to Search = 1
#   1) Find out pivot point and divide the array in two
#       sub-arrays. (pivot = 2) /*Index of 5*/
#   2) Now call binary search for one of the two sub-arrays.
#       (a) If element is greater than 0th element then
#              search in left array
#       (b) Else Search in right array
#           (1 will go in else as 1 < 0th element(3))
#   3) If element is found in selected sub-array then return index
#      Else return -1.
# Below is the implementation of the above approach:  


# Python Program to search an element
# in a sorted and pivoted array
 
# Searches an element key in a pivoted
# sorted array arrp[] of size n
def pivotedBinarySearch(arr, n, key):
 
    pivot = findPivot(arr, 0, n-1);
 
    # If we didn't find a pivot,
    # then array is not rotated at all
    if pivot == -1:
        return binarySearch(arr, 0, n-1, key);
 
    # If we found a pivot, then first
    # compare with pivot and then
    # search in two subarrays around pivot
    if arr[pivot] == key:
        return pivot
    if arr[0] <= key:
        return binarySearch(arr, 0, pivot-1, key);
    return binarySearch(arr, pivot + 1, n-1, key);
 
 
# Function to get pivot. For array
# 3, 4, 5, 6, 1, 2 it returns 3
# (index of 6)
def findPivot(arr, low, high):
     
    # base cases
    if high < low:
        return -1
    if high == low:
        return low
     
    # low + (high - low)/2;
    mid = int((low + high)/2)
     
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)
 
# Standard Binary Search function*/
def binarySearch(arr, low, high, key):
 
    if high < low:
        return -1
         
    # low + (high - low)/2;   
    mid = int((low + high)/2)
     
    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binarySearch(arr, (mid + 1), high,
                                            key);
    return binarySearch(arr, low, (mid -1), key);
 
 
# Driver program to check above functions */
# Let us search 3 in below array
arr1 = [5, 6, 7, 8, 9, 10, 1, 2, 3]
n = len(arr1)
key = 3
print("Index of the element is : ",
      pivotedBinarySearch(arr1, n, key))
       
# Output
# Index of the element is : 8
# Complexity Analysis:  

# Time Complexity: O(log n). 
# Binary Search requires log n comparisons to find the element. So time complexity is O(log n).
# Space Complexity: O(1), No extra space is required.

###################################################################################################################################

# Improved Solution: 
# Approach: Instead of two or more passes of binary search the result can be found in one pass of binary search.
#  The binary search needs to be modified to perform the search. The idea is to create a recursive function
#  that takes l and r as a range in input and the key.

# 1) Find middle point mid = (l + h)/2
# 2) If key is present at middle point, return mid.
# 3) Else If arr[l..mid] is sorted
#     a) If key to be searched lies in range from arr[l]
#        to arr[mid], recur for arr[l..mid].
#     b) Else recur for arr[mid+1..h]
# 4) Else (arr[mid+1..h] must be sorted)
#     a) If key to be searched lies in range from arr[mid+1]
#        to arr[h], recur for arr[mid+1..h].
#     b) Else recur for arr[l..mid] 
# Below is the implementation of the above idea:  


# Search an element in sorted and rotated array using
# single pass of Binary Search
 
# Returns index of key in arr[l..h] if key is present,
# otherwise returns -1

def Search(arr,n,k):
    #code here
    l = 0
    h = n-1
    
    while l <= h:
        m = (l + h) // 2
        if arr[m] == k:
            return m
        if arr[l] <= arr[m]: # If arr[l...mid] is sorted
            if arr[l] <= k  and k <= arr[m]:
                h = m-1
            else:
                l = m + 1
        else:
            if arr[m] <= k and k <= arr[h]:
                l = m+1
            else:
                h = m-1
    return -1


def search (arr, l, h, key):
    if l > h:
        return -1
     
    mid = (l + h) // 2
    if arr[mid] == key:
        return mid
 
    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:
 
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        return search(arr, mid + 1, h, key)
 
    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    return search(arr, l, mid-1, key)
 
# Driver program
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 3
i = search(arr, 0, len(arr)-1, key)
if i != -1:
    print ("Index: % d"% i)
else:
    print ("Key not found")
 
# This code is contributed by Shreyanshi Arun
# Output
# Index: 8
# Complexity Analysis: 

# Time Complexity: O(log n). 
# Binary Search requires log n comparisons to find the element. So time complexity is O(log n).
# Space Complexity: O(1). 
# As no extra space is required.

# How to handle duplicates? 
# It doesn’t look possible to search in O(Logn) time in all cases when duplicates are allowed. For example consider searching 0 in {2, 2, 2, 2, 2, 2, 2, 2, 0, 2} and {2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2}. 
# It doesn’t look possible to decide whether to recur for the left half or right half by doing a constant number of comparisons at the middle.
# Suppose you have a sorted array of infinite numbers, how would you search an element in the array?

# Source: Amazon Interview Experience.

# Since array is sorted, the first thing clicks into mind is binary search, but the problem here is that we don’t know size of array.
# If the array is infinite, that means we don’t have proper bounds to apply binary search. So in order to find position of key, first we find bounds and then apply binary search algorithm.

# Let low be pointing to 1st element and high pointing to 2nd element of array, Now compare key with high index element,
# ->if it is greater than high index element then copy high index in low index and double the high index.
# ->if it is smaller, then apply binary search on high and low indices found.

def search(arr,target):
    l,r=0,1
    while arr[r]<target:
        l,r=r,2*r
    return binSearch(l,r,arr,target)
def binSearch(l,h,arr,key):
    while l<=h:
        m=(l+h)//2
        if arr[m]== key:
            return arr[m]
        elif arr[m]>key:
            h=m-1
        else:
            l=m+1
    return -1
print(search([3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170] ,10))


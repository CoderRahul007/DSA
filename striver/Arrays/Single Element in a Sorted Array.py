
# every element is present twice except lucky number find that
def uniqueElement(arr, n):
    # Write your code here
    x = arr[0]
    for i in range(1 ,n):
        x= x^arr[i]
    return x

##################################################################
# Using binary search
 
# -- Intuition
# // choice 1
# -- if array is sorted and every element occurs twice then, it's obvious that for every EVEN i : arr[i] == arr[i+1] .
# -- it means unique value is after index "i+2"

# // choice 2
# -- but when a unique value is introduced, then the above pattern holds true only for array behind the unique value.
# -- after unique value for every ODD i : arr[i] == arr[i+1]
# -- it means unique value is before index "i"



 
"""
	Time Complexity  : O(log(N))
	Space Complexity : O(1)

	Where N is the total number of elements in the given array.
"""


def uniqueElement(arr, n):
    low = 0
    high = n - 1

        # Do binary search
    while (start < end):
        mid = start + (end-start)//2

        # handle when mid is odd
        if (mid % 2 != 0): #odd
            if (arr[mid] != arr[mid+1]):
                start = mid+1
            else:
                end = mid-1

        # handle when mid is even
        else:
            if (arr[mid] == arr[mid+1]):
                start = mid+2
            else:
                end = mid-1
    return arr[start]    
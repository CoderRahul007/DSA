# it means find the index of same element of just greater than the elemtent
def lower_bound(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= target: # here its greater than and equal
             # it means it can be the solution but we will search in left also since we have 
            # to find ether that value or just GREATER than that value
            result = mid
            right = mid - 1
        else: # is arr[mid] is less then target then lower bound is in the right part
            left = mid + 1

    return result

# it means find the index of same element of just less than the elemtent
def upper_bound(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] <= target: # here its lesss than and equal
            # it means it can be the solution but we will search in right also since we have 
            # to find ether that value  or just less than that value
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


# Test the functions
arr = [1, 2, 3, 6, 3, 4, 5]
target = 3

lower = lower_bound(arr, target)
upper = upper_bound(arr, target)

print("Lower bound:", lower)
print("Upper bound:", upper)

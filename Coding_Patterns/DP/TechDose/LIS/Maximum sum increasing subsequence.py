import sys


# Function to find the maximum sum of increasing subsequence
def MSIS(nums, i=0, prev=-sys.maxsize, total=0):

    # base case: nothing is remaining
    if i == len(nums):
        return total

    # case 1: exclude the current element and process the
    # remaining elements
    excl = MSIS(nums, i + 1, prev, total)

    # case 2: include the current element if it is greater
    # than the previous element

    if nums[i] > prev:  # if prev is less than current it means it can be added in subsequesnce
        incl = MSIS(nums, i + 1, nums[i], total + nums[i])
    else:  # if prev is greater than current it means it will not be added in solution
        incl = total

    # return the maximum of the above two choices
    return max(incl, excl)


def lis_from_last_element(arr, n):
    lis = [ele for ele in arr]
    for i in range(n-1, -1, -1):  # we are starting from
        # behind since from last element we check if there is an element greater
        # than that if not lis is 1 for all
        # and we use the lis of next element to evaluate the lis of
        # previous element and when all element are proccesed then we calculate max
        # for refernce refer neetcode
        for j in range(i+1, n):
            if arr[i] < arr[j]:
                include = arr[i] + lis[j]
                exclude = lis[i]
                lis[i] = max(include, exclude)
    m = max(lis)
    print(m)
    s = []
    for i in range(len(lis)):
        if lis[i] == m:
            s.append(arr[i])
            m -= arr[i]
    print(s)


arr = [10, 22, 9, 33, 21, 50, 41, 60]
lis_from_last_element(arr, len(arr))
print(MSIS(arr))

# Inversion Count for an array indicates – how far (or close) the array is from being sorted.
#  If the array is already sorted, then the inversion count is 0, but if the array is sorted 
# in the reverse order, the inversion count is the maximum. 
# Formally speaking, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j 
# Example: 

# Input: arr[] = {8, 4, 2, 1}
# Output: 6

# Explanation: Given array has six inversions:
# (8, 4), (4, 2), (8, 2), (8, 1), (4, 1), (2, 1).

# https://www.youtube.com/watch?v=owZhw-A0yWE


def merge( arr , left , mid , right):
    i = left
    j = mid
    k = 0

    invCount = 0

    temp = [0 for x in range(right - left + 1)]

    # boundary for two subarrays [left - mid ) [ mid - right]
    while i < mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            k+=1
            i+=1
        else:
            temp[k] = arr[j]
            invCount += mid - i # since all the items to the right of i will be greater than j index 
            k += 1
            j += 1
    
    while i < mid:
        temp[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1
    
    k = 0
    for i in range(left , right + 1):
        arr[i] = temp[k]
        k += 1
    return invCount




def mergeSort(arr , left , right):
    invCount = 0
    if right > left:
        mid = (left + right) >> 1

        invCount = mergeSort(arr , left , mid)
        invCount += mergeSort(arr , mid+1 , right)
        invCount += merge(arr , left , mid + 1, right)
    return invCount



arr = [1, 20, 6, 4, 5]
arr =[2 ,4, 1, 3, 5]
print(mergeSort(arr , 0 , len(arr) -1))







# I come across this problem for some times, As a whole, I think it should be still 
# ok to use quick sort to compute the inversion count,
#  as long as we do some modification to the original quick sort algorithm. (But I 
# have not verified it yet, sorry for that).

# Consider an array 3, 6, 2, 5, 4, 1. Support we use 3 as the pivot, the most voted
#  answer is right in that the exchange might 
# mess the orders of the other numbers. However, we might do it different by introducing 
# a new temporary array:

#     Iterates over the array for the first time. During the iteration, moves all the
#  numbers less than 3 to the temporary array. 
# For each such number, we also records how much number larger than 3 are before it.
#  In this case, the number 2 has one number 6 before it,
#  and the number 1 has 3 number 6, 5, 4 before it. This could be done by a simple counting.
#     Then we copy 3 into the temporary array.
#     Then we iterates the array again and move the numbers large than 3 into the 
# temporary array. At last we get 2 1 3 6 5 4.

# The problem is that during this process how much inversion pairs are lost? 
# The number is the sum of all the numbers in the first step, 
# and the count of number less than the pivot in the second step. Then we have
#  count all the inversion numbers that one is >= pivot and another is < pivot.
#  Then we could recursively deal with the left part and the right part.


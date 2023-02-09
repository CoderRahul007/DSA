def findMinima(arr):
    n = len(arr)
    l = 0
    r = n-1
    while l <= r:
        mid = (l + r) >> 1

        if (mid == 0 or arr[mid-1] > arr[mid]) and (mid == n-1 or arr[mid] < arr[mid+1] ):
            break
        if mid > 0 and arr[mid-1] < arr[mid]:
            l = mid+1
        else:
            r = mid-1
    return mid

arr = [ 1, 3, 20, 4, 1, 0 ]
print(findMinima(arr))


    
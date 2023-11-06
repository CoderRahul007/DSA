def first_occur( arr , ele):
    start = 0
    high = len(arr) -1
    res = -1
    while start <= high:
        mid = start + (high - start) //2
        if arr[mid] == ele:
            res = mid
            end = mid -1 # left search space
        elif arr[mid] < ele:
            start = mid + 1
        else:
            end = high -1
    return res


def last_occur( arr , ele):
    start = 0
    high = len(arr) -1
    res = -1
    while start <= high:
        mid = start + (high - start) //2
        if arr[mid] == ele:
            res = mid
            start = mid + 1 # right search space
        elif arr[mid] < ele:
            start = mid + 1
        else:
            end = high -1
    return res

arr  = [ 1 ,2 , 3 , 4 , 10 , 10 , 10 , 15 ,20]
print(first_occur(arr , 10))
print((last_occur(arr , 10)))
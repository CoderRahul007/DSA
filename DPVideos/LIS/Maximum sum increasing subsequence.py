def MSIS(arr):
    msis = [0]*len(arr)
    for i in range(len(arr)):
        msis[i] = arr[i]

    for i in range(1 , len(arr)):
        for j in range(i):
            if arr[i] > arr[j] and msis[i] < arr[i] + msis[j]:
                msis[i] = arr[i] + msis[j]
    print(max(msis))
    print(msis)
    m = max(msis)
    l = []
    for i in range(len(arr)-1 , -1 , -1):
        if m == msis[i]:
            m -= arr[i]
            l.append(arr[i])
    print(l[::-1])

arr = [1 , 101 , 2 ,3 , 100 , 4 , 5]
# Time Complexity: O(n^2) 

# Space Complexity O(n) 

MSIS(arr)


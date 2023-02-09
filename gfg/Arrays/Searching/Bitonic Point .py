def findMaximum(arr, n):
    # code here
    l = 0
    r = n-1
    
    while l <= r:
        m = (l+r)>>1
        if m == n-1 :
            if arr[m-1] < arr[m]:
                return arr[m]
        elif arr[m-1] < arr[m] > arr[m+1]:
            return arr[m]
        elif arr[m] < arr[m+1] and m < n-1:
            l = m+1
        else :
            r = m-1
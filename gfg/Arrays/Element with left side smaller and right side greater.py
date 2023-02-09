def findElement( arr, n):
    minl = [0]*n
    maxl = [0]*n
    
    minl[0] = arr[0]
    maxl[n-1] = arr[n-1]
    for i in range(1 , n):
        minl[i] = max(minl[i-1] , arr[i])
    for i in range(n-2 , -1 , -1):
        maxl[i] = min(maxl[i+1] , arr[i])
    
    for i in range(1 , n-1):
        if arr[i] >= minl[i-1] and arr[i] <= maxl[i+1]:
            return arr[i]
    
    return -1
    
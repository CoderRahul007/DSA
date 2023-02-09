def find3numbers(arr):
    n = len(arr)

    leftmin = [0]*n
    rightmax = [0]*n

    leftmin[0] = -1

    mini = 0

    # Create an array that will store 
    # index of a smaller element on left side. 
    # If there is no smaller element on left side,
    # then smaller[i] will be -1.
    for i in range(1 , n):
        if arr[mini] >= arr[i]:
            mini = i
            leftmin[i] = -1
        else:
            leftmin[i] = mini
    
    rightmax[n-1] = -1
    maxi = n-1

    for i in range(n-2 , -1 , -1):
        if arr[i] >= arr[maxi]:
            maxi = i
            rightmax[i] = -1
        else:
            rightmax[i] = maxi
    
    out = []
    for i in range(n):
        if rightmax[i] != -1 and leftmin[i] != -1 :
            out.append((arr[leftmin[i]] , arr[i] , arr[rightmax[i]]))
    return out
    

#  https://www.geeksforgeeks.org/find-a-sorted-subsequence-of-size-3-in-linear-time/    


#  https://stackoverflow.com/questions/10008118/how-to-find-3-numbers-in-increasing-order-and-increasing-indices-in-an-array-in
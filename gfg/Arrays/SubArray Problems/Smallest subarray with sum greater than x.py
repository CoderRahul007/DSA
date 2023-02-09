

# sliding windows
def smallestSubWithSum(arr , n , x):
    s = 0
    left = 0
    ans = n
    for i in range(n):
        s += arr[i]
        if s > x:
            while s-arr[left] > x:            
                s -= arr[left]
                left += 1
            ans = min(ans , i - left + 1)
    return ans
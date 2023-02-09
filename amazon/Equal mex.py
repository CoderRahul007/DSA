def equalMex( N   , A):
    MOD = 998244353
    idx = [0]*N
    for i in range(N):
        idx[A[i]] = i
    
    l = idx[0]
    r = idx[0]
    ans = 1
    m = 1
    Set = set()
    Set.add(0)
    cnt = 1
    while m < N:
        cnt +=1
        while idx[m] < l:
            l-=1
            Set.add(A[l])
        while idx[m] > r:
            r+=1
            Set.add(A[r])
        m += 1
        t = 0
        while m in Set:
            m += 1
            t += 1
        len = r - l +1
        len -= cnt
        for i in range(t):
            ans = (ans * len) % MOD
            len -=1
        cnt += t
    return ans
            





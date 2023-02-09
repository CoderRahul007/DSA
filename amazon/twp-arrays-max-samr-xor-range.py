def twoArrays(N , A , B):
    aa = 0
    bb = 0
    mp = {}
    ans = 0
    for i in range(n):
        aa = aa ^ A[i]
        bb = bb ^ B[i]
        if aa ^ bb in mp:
            ans = max(ans , i - mp[aa ^ bb] + 1)
        else:
            mp[aa ^ bb] = 1
    return ans



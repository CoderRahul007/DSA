# https://www.youtube.com/watch?v=muDPTDrpS28&t=666s
def reach( arr ):
    n = len(arr)
    reachable = 0
    for i in range(n):
        if reachable < i:
            return False
        reachable = max(reachable , arr[i] + i)
    return True

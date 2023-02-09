def countPairs(arr , s):
    map = {}
    c = 0
    for i in range(len(arr)):
        if s-arr[i] in map:
            c+= map[s-arr[i]]
        if arr[i] in map:
            map[arr[i]] +=1
        else:
            map[arr[i]] = 1
    return c

arr = [1, 5, 7, -1, 5]

sum = 6
print(countPairs(arr , sum))

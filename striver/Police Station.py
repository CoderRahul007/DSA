# https://www.youtube.com/watch?v=7JwGNqNDevM&list=PLQQzQd5Y8oSLv-X52FbzxXQx1pGj4Vh4X

from collections import defaultdict
def police(arr , a):
    mp = defaultdict(lambda : 0)
    m = 0
    for i in arr:
        t = abs(i-a)
        mp[t] +=1

        


arr = [4 , 5 , -5]
a = 1
print(police(arr, a))
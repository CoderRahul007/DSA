from os import *
from sys import *
from collections import *
from math import *

from typing import List

from heapq import heappop , heappush , heapify
from collections import defaultdict


def KMostFrequent(n: int, k: int, arr: List[int]) -> List[int]:
    # write your code here
    hp = []
    ans = []
    mp = defaultdict(lambda : 0)
    for i in arr:
        mp[i] += 1
    for key , v in mp.items():
        heappush(hp , (-v , key))
    while len(hp) > 0 and k > 0:    
        t = heappop(hp)
        ans.append(t[1])
        k-=1    
    ans.sort()
    return ans
        

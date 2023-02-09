import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = dict()
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        heap = []
        for key,val in mp.items():
            heapq.heappush(heap,(val, key))     
            if len(heap) > k:
                heapq.heappop(heap)

        return [el[1] for el in heap]

###################################################################################################

# Time complexit: O(n**2)

# O(nlogn) + O(n*m) -> max(O(nlogn), O(n*m))->max(O(nlogn), O(n**2))
# n is the length of all events, m is the biggest size of the heap, because the biggest m=n//2, the number of start events equals to end events.

# create and sort events list: O(nlogn)
# iterate the events list: O(n)
# add an item into the heapO(logm)
# pop off the largest one in the heap O(1)
# delete a specific item in the heap by iterating the heap
# and heapify the heap again O(m)+O(m)
# Cons:
# When encounter the end point to delete a specific item from heap, I do the linear search to locate it and delete it, which takes O(m) time. 
# After doing this, the list is not sorted in a heapify way, so the list needs to be heapified again which takes O(m) time.

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        start_events = [(s, -h) for s,_, h in buildings]
        end_events = [(e, h) for _, e, h in buildings]
        events = start_events+end_events
        events.sort()
        maxh = []
        heapq.heappush(maxh, 0)
        ans = []
        previous_h = 0
        for t, h in events:
            if h < 0:
                # a new building comes in
                heapq.heappush(maxh, h)
                if maxh[0] != previous_h:
                    ans.append([t, -h])
                    previous_h = h
                else:
                    continue
            else:
                # a building ends
                cur_h = -h
                maxh = self.deleteHightinHeap(maxh, cur_h)
                if maxh[0] != previous_h:
                    ans.append([t, -maxh[0]])
                    previous_h = maxh[0]
        return ans
                
    def deleteHeightinHeap(self, maxh, height):
        maxh.remove(height) # delete the item-> O(m), m is the biggest size of the heap
        heapq.heapify(maxh) # heapify the maxh list again-> O(m)
        return maxh

#################################################################################################################


# Time complexity: O(nlogn)

# O(nlogn)+O(n*logm) -> max(O(nlogn), O(nlogm)) -> O(nlogn)
# n is the length of all events, m is the biggest size of h, because the biggest m=n//2, the number of start events equals to end events.

# create and sort events list: O(nlogn)
# iterate the events list: O(n)
# add an item into the listO(logm)
# pop off the largest one from the list O(1)
# delete a specific item in the list by binary searching it O(logm)

# Solution to optimize delete operation:
# Use bisect, when insert a new item into the ordered list or delete a specific item from the list,
#  it only takes O(logm) time, since it is doing binary search to locate needed position internally.

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h))
            events.append((r, h))
        events.sort()
        
        h = [0]
        previous_h = 0
        ans = []

        for x, cur_h in events:

            if cur_h < 0: # start point
                actual_height = -cur_h
                if actual_height > previous_h:
                    previous_h = actual_height
                    ans.append([x, actual_height])
                bisect.insort_right(h, actual_height) # bisect.insort_left(h, actual_height) also can work, as long as after insertion the list is ordered  

            else: # end point
                h.pop(bisect.bisect_left(h, cur_h)) # leftmost cur_h in h list                
                last_height = h[-1]

                if last_height < previous_h:
                    previous_h = last_height
                    ans.append([x, last_height])
        return ans

###################################################################################
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
            Observation:
                1. The start point of all the buildings could be a potential key point.
                2. The end point of all the buildings could be a potential key point.
                3. Sort these points based on start point then by their respective height so that while
                 iteratng we can be assure that for same starting point, we will at max height point first. 
                4. Track the maxHeight while iterating and for any point the maxHeight changes then that point is a key point.
        """
        points = []
        for s,e,h in buildings:
            points.append([s, e, -h])
            # Height is taken as zero so as to distinguish between starting and ending point.
            points.append([e, 0, 0])
        
        points.sort(key=lambda x: (x[0],x[2],x[1]))
        
        keyPoints = [[0,0]] # start , height
        heap = [[0, sys.maxsize]]       # height , end point  
        for s,e,h in points:
            # Pop out the buildings which are already left behind.
            while heap and heap[0][1] <= s: #  max height end point <= start point
                heapq.heappop(heap)
            
            # If the current point is the start point of any building then push it to heap.
            if h != 0:
                heapq.heappush(heap, [h, e])
            
            # If by pushing the current point into heap, the maxHeight changed, then include the current point in answer
            if keyPoints[-1][1] != -heap[0][0]:
                keyPoints.append([s, -heap[0][0]])
            
        return keyPoints[1:]
            
            
# https://www.youtube.com/watch?v=POUMNJou4vc            

# n logn n
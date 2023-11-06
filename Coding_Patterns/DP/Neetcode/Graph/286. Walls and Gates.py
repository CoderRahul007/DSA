# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example: 

# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4


from typing import (
    List,
)

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def walls_and_gates(self, rooms: List[List[int]]):
        # write your code here
        ROWS = len(rooms)
        COLS = len(rooms[0])

        visit = set()
        q = deque()
        
        def addRooms( r , c):
            if (r , c) in visit or r not in range(ROWS) or c not in range(COLS) or rooms[r][c] == -1:
                continue
            visit.add((r,c))
            q.append([r,c])

        for i in  range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))
        
        dist = 0
        while q:
            for i in range(q):
                r,c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1 , c)
                addRooms(r - 1 , c)
                addRooms(r , c + 1)
                addRooms(r , c - 1)
            dist += 1 # first we will process all the gates and their value will always be 0
            # after that we are incrementing to get all the cells with 1 or subsequent dist from the gates
            


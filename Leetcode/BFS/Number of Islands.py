###########################################################################################
# DFS

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # dfs search
        def dfs(i, j):
            if m <= i or i < 0 or n <= j or j < 0 or grid[i][j] != '1':
                return

            grid[i][j] = 'X'
            for x1, y1 in directions:
                dfs(i + x1, j + y1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': 
                    count += 1
                    dfs(i, j)
        return count

##################################################################################################
# BFS 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M, N = len(grid), len(grid[0])        
        def bfs(i, j):
            q = collections.deque([(i, j)])
            visited.add((i, j))
            while q:
                r, c = q.popleft() # for making DFS make it to pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr == M or nc < 0 or nc == N:
                        continue
                    if grid[nr][nc] == '0' or (nr, nc) in visited:
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))
            return None

        visited = set()
        islands = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '0' or (i, j) in visited:
                    continue
                bfs(i, j)
                islands += 1
        return islands
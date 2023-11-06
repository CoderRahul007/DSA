# You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) and 1's (representing land). An island is a group of 1's connected 4-directionally (horizontal or vertical). Any cells outside of the grid are considered water cells.

# An island in grid2 is considered a sub-island if there is an island in grid1 that contains all the cells that make up this island in grid2.

# Return the number of islands in grid2 that are considered sub-islands

# Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# Output: 3
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
# Example 2:


# Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
# Output: 2
# Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
# The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        h = len(grid1)
        w = len(grid1[0])

        seen = set()
        sub_island = 0

        for i in range(h):
            for j in range(w):
                if grid2[i][j] and (i, j) not in seen:
                    same = grid2[i][j] == grid1[i][j]
                    to_visit = [(i, j)]
                    seen.add((i, j))
                    while to_visit:
                        ii, jj = to_visit.pop()
                        for r, c in [(ii + 1, jj), (ii - 1, jj), (ii, jj + 1), (ii, jj - 1)]:
                            if 0 <= r < h and 0 <= c < w and (r, c) not in seen and grid2[r][c]:
                                if grid2[r][c] != grid1[r][c]:
                                    same = False
                                to_visit.append((r, c))
                                seen.add((r, c))
                    if same:
                        sub_island += 1

        return sub_island

# Given a 2D grid of n*m of characters and a word, find all occurrences
#  of given word in grid. A word can be matched in all 8 directions
#  at any point. Word is said be found in a direction if all characters 
# match in this direction (not in zig-zag form). The 8 directions are,
#  horizontally left, horizontally right, vertically up, vertically down
#  and 4 diagonal directions.
 

# Example 1:

# Input: grid = {{a,b,c},{d,r,f},{g,h,i}},
# word = "abc"
# Output: {{0,0}}
# Explanation: From (0,0) one can find "abc"
# in horizontally right direction.

# Example 2:

# Input: grid = {{a,b,a,b},{a,b,e,b},{e,b,e,b}}
# ,word = "abe"
# Output: {{0,0},{0,2},{1,0}}
# Explanation: From (0,0) one can find "abe" in 
# right-down diagonal. From (0,2) one can
# find "abe" in left-down diagonal. From
# (1,0) one can find "abe" in Horizontally right 
# direction.


####################################################################################

# If zig-zag pattern was allowed

# int n = M.size(), m = M[0].size();
# 	    vector <pair<int,int>> d {{0,1}, {0,-1}, {1,0}, {-1,0}, {1, 1}, {-1,-1}, {1,-1}, {-1,1}};
# 	    vector <vector<int>> v;
# 	    for(int i=0; i<n; i++){
# 	        for(int j=0; j<m; j++){
# 	            int idx = 0;
# 	            if(word[idx] != M[i][j])
# 	                continue;
# 	            vector <vector<bool>> vis(n, vector<bool> (m,0));
# 	            queue <pair<int,int>> q;
# 	            q.push({i,j});
# 	            while(!q.empty()){
# 	                idx += 1;
# 	                pair <int,int> p = q.front();
# 	                q.pop();
# 	                if(word[idx] == '\0'){
# 	                    v.push_back({i,j});
# 	                    break;
# 	                }
# 	                vis[p.first][p.second] = true;
# 	                for(auto k:d){
# 	                    int x = p.first  + k.first ;
# 	                    int y = p.second + k.second;
# 	                    if(x >= 0 && x < n && y >= 0 && y < m && vis[x][y] == false && M[x][y] == word[idx]){
# 	                        q.push({x,y});
# 	                    }
# 	                }
# 	                vis[p.first][p.second] = false;
# 	            }
# 	        }
# 	    }
# 	    return v;

class Solution:
    
        def __compare_direction_substring(self, i, j, k, offset_row, offset_col, n, grid, word):
            while (k < n):
                if (grid[i][j] != word[k]):
                    return False
                i += offset_row ; j += offset_col ; k += 1
            return True    

        def searchWord(self, grid, word):
            # Code here
            r, c, n = len(grid), len(grid[0]), len(word)
            offsets = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1))
            idx_within_range = lambda idx, start, end : start <= idx < end
            res = []
            for i in range(r):
                for j in range(c):
                    if (grid[i][j] == word[0]):
                        for offset_row, offset_col in offsets:

                            end_pos_row, end_pos_col = (i + ((n - 1) * offset_row)), (j + ((n - 1) * offset_col)) # means if offset row and col is added to i and j len(word) -1 times will it be in range or not
                            if (idx_within_range(end_pos_row, 0, r) and idx_within_range(end_pos_col, 0, c)):
                                if (self.__compare_direction_substring((i + offset_row), (j + offset_col), 1, offset_row, offset_col, n, grid, word)):
                                    res.append([i, j])
                                    break
            return res

# Expected Time Complexity: O(n*m*k) where k is constant
# Exected Space Complexity: O(1)
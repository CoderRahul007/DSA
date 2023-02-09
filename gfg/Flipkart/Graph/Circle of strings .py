# Given an array of lowercase strings A[] of size N, determine 
# if the strings can be chained together to form a circle.
# A string X can be chained together with another string Y 
# if the last character of X is same as first
# character of Y. If every string of the array can 
# be chained, it will form a circle.

# For example, for the array arr[] = {"for", "geek", "rig", "kaf"} 
# the answer will be Yes as the given strings can be chained as 
# "for", "rig", "geek" and "kaf"

# https://www.geeksforgeeks.org/given-array-strings-find-strings-can-chained-form-circle/

# Example 1:

# Input:
# N = 3
# A[] = { "abc", "bcd", "cdf" }
# Output:
# 0
# Explaination:
# These strings can't form a circle 
# because no string has 'd'at the starting index.

# Example 2:

# Input:
# N = 4
# A[] = { "ab" , "bc", "cd", "da" }
# Output:
# 1
# Explaination:
# These strings can form a circle 
# of strings.


# class Solution
# {
#     int graph[26][26];
#     void dfs(int v, vector<bool> &visited)
#     {
#         visited[v] = true;
#         for(int i=0 ; i<26 ; i++)
#             if(graph[v][i] && !visited[i])
#                 dfs(i,visited);
#     }
#     public:
#     int isCircle(int N, vector<string> A)
#     {
#         memset(graph,0,sizeof(graph));
#         vector<int> in(26,0);
#         vector<int> out(26,0);
#         for(int i=0 ; i<N ; i++)
#         {
#             int a = A[i][0] - 'a';
#             int b = A[i].back() - 'a';
#             in[a]++;
#             out[b]++;
#             graph[a][b] = 1;
#         }
#         for(int i=0 ; i<26 ; i++)
#             if(in[i] != out[i])
#                 return 0;
#         vector<bool> visited(26,false);
#         int i;
#         for(i=0 ; i<26 ; i++)
#             if(in[i])
#                 break;
#         dfs(i,visited);
#         for(int i=0 ; i<26 ; i++)
#             if(in[i] && visited[i] == false)
#                 return 0;
#         return 1;
#     }
# };
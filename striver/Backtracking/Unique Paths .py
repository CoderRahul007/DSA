# Problem Statement
# You are present at point ‘A’ which is the top-left cell of an M X N matrix, 
# your destination is point ‘B’, which is the bottom-right cell of the same matrix. 
# Your task is to find the total number of unique paths from point ‘A’ to point ‘B’.
# In other words, you will be given the dimensions of the matrix as integers ‘M’ and ‘N’,
#  your task is to find the total number of unique paths from the cell MATRIX[0][0] to MATRIX['M' - 1]['N' - 1].
# To traverse in the matrix, you can either move Right or Down at each step.
#  For example in a given point MATRIX[i] [j], you can move to either MATRIX[i + 1][j] or MATRIX[i][j + 1].
# Input Format:

# The first line of input contains an integer 'T' representing the number of the test case. 

# The first and the only line of each test case contains two space-separated integers ‘M’ and ‘N’,
#  denoting the number of rows and number of columns of the matrix respectively. 

# Output Format:

# For every test case, return a single integer, which is the total number of unique paths
#  for traveling from top-left to bottom-right cells of the matrix.

# The output of each test case is printed in a separate line.

# Note:

# You don’t have to print anything, it has already been taken care of. Just implement the given function. 

###########################################################################################################3

#  Recursive Approach
# We can easily count the total number of paths by making a recursive algorithm.

# The steps are as follows:

# We are given a function UNIQUEPATHS(), which takes two integers ‘M’ and ‘N’ as parameters and returns a single integer. This will be the definition of our recursive function too.
# As our base condition, we will check if our number of rows (‘M’) or a number of columns (‘N’) is equal to 1. If either one of them is equal to 1, this will mean that it is a 1-D array, and only a single path will be available. Hence we will return 1.
# If our base condition is not satisfied, we will proceed by calling our recursive function, UNIQUEPATHS() by providing it with the left and upper submatrix. Hence we will return UNIQUEPATHS('M', ‘N’ - 1) + UNIQUEPATHS('M' - 1, ‘N’).
# After all the recursive calls, the function UNIQUEPATHS() will return the final answer.
# Time Complexity
# O(2 ^ (M + N)), Where ‘M’ is the number of rows and ‘N’ is the number of columns of the matrix.
# Since for every recursive call, two more recursive calls are taking place. Thus the worst-case time complexity will be O(2 ^ (M + N)).
# Space Complexity
# O(max(M, N)), where M is the number of rows and N is the number of columns of the matrix
# Since due to the recursion stack space, the space complexity will be O(max(M, N)).

"""
    Time Complexity  : O(2 ^ (M + N)) 
    Space Complexity : O(max(M,N))
    
    Where 'M' is the number of rows and 'N' is the number of columns of the matrix.    
"""
# Top Down Approach
def uniquePaths(m, n):
    
	# Base condition.
    if(m == 1 or n == 1):            
	    return 1

	# Recursive call.
    return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)  

#########################################################################################################################

"""
    Time Complexity  : O(M * N) 
    Space Complexity : O(M * N)
    
    Where 'M' is the number of rows and 'N' is the number of columns of the matrix.   
"""

def uniquePathsHelper(m, n, lookupTable):

    # Base condition.
    if(m == 1 or n == 1):           
        return 1
    
    # Check for solved subproblems.
    if(lookupTable[m][n] != -1):    
        return lookupTable[m][n]

    # Recursive call.
    temp = uniquePathsHelper(m - 1, n, lookupTable) + uniquePathsHelper(m, n - 1, lookupTable)
    lookupTable[m][n] = temp
    
    return temp                  

def uniquePaths(m, n):
    
    # Lookup table.
    lookupTable = [[-1 for i in range(n+1)] for j in range(m+1)]      

    # Calling helper function.
    return uniquePathsHelper(m,n,lookupTable)

# O(M * N), Where ‘M’ is the number of rows and ‘N’ is the number of columns of the matrix
# Since the recursive approach will do the work in the order M * N. Thus the worst-case time complexity will be O(M * N).
# Space Complexity
# O(M * N), Where ‘M’ is the number of rows and ‘N’ is the number of columns of the matrix.
# Since the lookup table takes the space of M * N cells and thus the space complexity will be O(M * N).
#############################################################################################################################

def uniquePaths(m, n):

    # Reference table to store subproblems.
    dp = [[0 for i in range(n)] for j in range(m)]                  

    # Paths to reach a cell in column 1.
    for i in range(m):
        dp[i][0] = 1
    
    # Paths to reach a cell in row 1.
    for j in range(n):  
        dp[0][j] = 1
    
    # Bottom up approach.
    for i in range(1, m):  
        for j in range(1, n):  
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 

    # Returning answer.
    return dp[m - 1][n - 1] 
###################################################################################################################################3

#  Dynamic Programming Space optimized

# The previous approach improved our solution to a large extent by avoiding the common subproblem recomputations. But the space complexity can be even further improved as the results of subproblems can also be stored in a 1-D array.

 

# The steps are as follows:

 

# We are given a function UNIQUEPATHS(), which takes two integers ‘M’ and ‘N’ as parameters and returns a single integer. This will be the definition of our recursive function too.
# Create a temporary 1-D array ‘DP’ of size ‘N’, which is the number of rows of the matrix. Initialise every element of the array as 1.
# Now we apply the Dynamic Programming approach, we will first store ‘DP[0]’ = 1 as our base problem. Then using the bottom-up recursive approach we will find the count of paths to reach other cells by using the values of subproblems.
# Finally, we will return the value of the last cell, which is ‘DP[[N - 1]’ as our final answer.

# Time Complexity

# O(M * N), Where ‘M’ is the number of rows and ‘N’ is the number of columns of the matrix.

 

# Since we are running a nested loop  M * N times, Thus the time complexity will be O(M * N).
# Space Complexity

# O(N), Where ‘N’ is the number of columns of the matrix

 

# Since we are storing elements in an array of size N, Thus the space complexity will be O(N).

"""
    Time Complexity  : O(M * N) 
    Space Complexity : O(N)
    
    Where 'M' is the number of rows and 'N' is the number of columns of the matrix.   
"""

def uniquePaths(m, n):

    # Reference array to store subproblems.
    dp = [0 for i in range(n)]                  

    dp[0] = 1

    # Bottom up approach.
    for i in range(m): 

        for j in range(1, n):
            dp[j] += dp[j - 1]
        
    # Returning answer.
    return dp[n - 1]                  


# https://takeuforward.org/data-structure/grid-unique-paths-dp-on-grids-dp8

# import java.util.*;

# class TUF{
# static int countWaysUtil(int m, int n, int[][] dp) {
 
#  for(int i=0; i<m ;i++){
#       for(int j=0; j<n; j++){
          
#           //base condition
#           if(i==0 && j==0){
#               dp[i][j]=1;
#               continue;
#           }
          
#           int up=0;
#           int left = 0;
          
#           if(i>0) 
#             up = dp[i-1][j];
#           if(j>0)
#             left = dp[i][j-1];
            
#           dp[i][j] = up+left;
#       }
#   }
  
#   return dp[m-1][n-1];

# }

# static int countWays(int m, int n){
#     int dp[][]=new int[m][n];
#     for (int[] row : dp)
#         Arrays.fill(row, -1);
#     return countWaysUtil(m,n,dp);
    
# }

# public static void main(String args[]) {

#   int m=3;
#   int n=2;
  
#   System.out.println(countWays(m,n));
# }
# }


##############################################################################################################################

# If we closely look the relation,

# dp[i][j] = dp[i-1][j] + dp[i][j-1])

# We see that we only need the previous row and column, in order to calculate dp[i][j]. Therefore we can space optimize it.

# Initially, we can take a dummy row ( say prev) and initialize it as 0.

# Now the current row(say temp) only needs the previous row value and the current row’s value in order to calculate dp[i][j].



# At the next step, the temp array becomes the prev of the next step and using its values we can still calculate the next row’s values.



# At last prev[n-1] will give us the required answer.

# Code:

# import java.util.*;

# class TUF{
# static int countWays(int m, int n){
#     int prev[]=new int[n];

#     for(int i=0; i<m; i++){
#         int temp[]=new int[n];
#         for(int j=0; j<n; j++){
#             if(i==0 && j==0){
#                 temp[j]=1;
#                 continue;
#             }
            
#             int up=0;
#             int left =0;
            
#             if(i>0)
#                 up = prev[j];
#             if(j>0)
#                 left = temp[j-1];
                
#             temp[j] = up + left;
#         }
#         prev = temp;
#     }
    
#     return prev[n-1];
    
# }

# public static void main(String args[]) {

#   int m=3;
#   int n=2;
  
#   System.out.println(countWays(m,n));
# }
# }
# Output:

# 3

# Time Complexity: O(M*N)

# Reason: There are two nested loops

# Space Complexity: O(N)

# Reason: We are using an external array of size ‘N’ to store only one row.
# Problem Statement
# You have been given a 2-D array 'MAT' of size M x N where 'M' and 'N'
#  denote the number of rows and columns, respectively. The elements of 
# each row are sorted in non-decreasing order.
# Moreover, the first element of a row is greater than the last element 
# of the previous row (if exists).
# You are given an integer 'TARGET' and your task is to find if it exists
#  in the given 'MAT' or not.
# Example :

# Given Matrix : 1 1 and Target : 8
#                4 8 

# The output should be "TRUE" as 8 is present in the Matrix.

# Input Format :

# The first line of input contains an integer 'T' representing the number
#  of test cases Then the test case follows :

# The first line of each test case contains three space-separated integers 
# 'M', 'N' and 'TARGET' where 'M' and 'N' denote the number of rows and columns 
# of the 'MAT', respectively and 'TARGET' is the integer to be found.

# From the second line of each test case, the next 'N' lines represent the 
# rows of the 'MAT'. Every row contains 'M' single space-separated integers.

# Output Format :

# For each test case, print “TRUE” if 'TARGET' is present in the 'MAT', else print “FALSE”.
############################################################################################################

'''
    O(M+N)
'''
def findTargetInMatrix(mat, m, n, target):
	# Write your code here.
    i = 0
    j = n-1 # start from top right of mat
    while i < m and j >=0:
        if mat[i][j] == target :
            return True
        elif mat[i][j] > target:
            j-=1
        else:
            i+=1
    return False


##############################################################################################################
# Since every row of the given matrix is sorted and the first element of row ‘i’  is greater than the last element of row  ‘i-1’  (if exist),
#  all the M*N elements of the matrix are arranged in an ascending order. 
# The intuition behind this approach is that since we can map indices of a matrix to an array, 
# we can treat the given matrix as an array/list of M*N sorted integers.  
# We map the indices of matrix elements to a 1D array as follows :  

#     If we copy the elements of a matrix (say ‘MAT’) to an array (say ‘ARR’) in a row-wise manner,
#  then the element ‘MAT[i][j]' is equal to ‘ARR[N*i+j]’, where ‘N’ denotes the number of columns in ‘MAT’.
#     Similarly, converting ‘ARR’ back to ‘MAT’, the element ‘ARR[i]’ is equal to ‘MAT[i/N][i%N]’
#  as ‘ARR’ contains M*N elements, so ‘rowNum’ is equal to i/N and ‘colNum' is equal to i%N.

 

# Now, we simply use binary search to find the ‘TARGET’.
# Time Complexity

# O(log(M*N)), ‘M’ and ‘N’ denote the number of rows and columns in ‘MAT’, respectively.

 

# We are applying binary search on over a range of M*N elements.
# Space Complexity

# O(1).
 

# Since, we are not using any extra space to find the number of pairs. Therefore, the overall space complexity will be O(1).
'''
    Time Complexity: O(log(M*N))
    Space Complexity: O(1)

    Where M and N are the number of rows and columns.
'''


def findTargetInMatrix(mat, m, n, target):

    start, end = 0, m * n - 1
    # m row , n col
    # Binary search.
    while start <= end:
        
        mid = start + (end - start) // 2
        val = mat[mid // n][mid % n] # as ‘ARR’ contains M*N elements, so ‘rowNum’ is equal to i/N and ‘colNum' is equal to i%N.
        # row -> div by n -> m*n // n -> gives m 
        # col -> rem by n -> m*n %n -> 
        if target < val:
            end = mid - 1

        elif target > val:
            start = mid + 1

        else:
            return True

    return False
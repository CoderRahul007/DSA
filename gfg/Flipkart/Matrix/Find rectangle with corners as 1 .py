#  Scan from top to down, line by line
# – For each line, remember each combination of 2 1’s and push that into a hash-set
# – If we ever find that combination again in a later line, we get our rectangle

# Time Complexity: O(n*m^2)

# Given a NxM binary matrix consisting of 0s and 1s. Find if there exists a rectangle/ square within the matrix whose all four corners are 1. 

# Example 1:

# Input:
# N = 4, M = 5
# matrix[][] = 
# {
# {1 0 0 1 0},
# {0 0 1 0 1},
# {0 0 0 1 0}, 
# {1 0 1 0 1}
# } 

# Output: Yes
# Explanation:
# Valid corners are at index (1,2), (1,4), (3,2), (3,4) 
class Solution:    
    def ValidCorner(self,matrix): 
        # Your code goes here 
        rows = len(matrix) 
        if (rows == 0): 
            return False
      
        columns = len(matrix[0]) 
      
        # map for storing the index of  
        # combination of 2 1's  
        table = {} 
      
        # scanning from top to bottom  
        # line by line  
        for i in range(rows):  
            for j in range(columns - 1): 
                for k in range(j + 1, columns):  
      
                    # if found two 1's in a column  
                    if (matrix[i][j] == 1 and
                        matrix[i][k] == 1): 
      
                        # check if there exists 1's in same  
                        # row previously then return true  
                        if (j in table and k in table[j]): 
                            return True
      
                        if (k in table and j in table[k]): 
                            return True
      
                        # store the indexes in hashset  
                        if j not in table: 
                            table[j] = set() 
                        if k not in table: 
                            table[k] = set() 
                        table[j].add(k)  
                        table[k].add(j) 
        return False

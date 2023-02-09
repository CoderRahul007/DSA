# You are given an integer N. Your task is to return a 2-D ArrayList containing 
# the pascal’s triangle till the row N.
# A Pascal's triangle is a triangular array constructed by summing adjacent elements
#  in preceding rows. Pascal's triangle contains the values of the binomial coefficient.
#   For example in the figure below.

# For example, given integer N= 4 then you have to print.

# 1  
# 1 1 
# 1 2 1 
# 1 3 3 1

# Here for the third row, you will see that the second element is the summation of 
# the above two-row elements i.e. 2=1+1, and similarly for row three 3 = 1+2 and 3 = 1+2.

def printPascal(n:int):
    # Write your code here.
    # Return a list of lists.
    out = []
    out.append([1])
    
    i = 1
    while i < n:
        prev = out[i-1]
        line = [1]
        for j in range(i-1):
            line.append(prev[j] + prev[j+1])
        line.append(1)
        out.append(line)
        i+=1
    return out

# Time - O(n^2)
# Space - O(n^2)

#####################################################################

# Using the property of coefficients.

# The idea is to use the property of pascal’s triangle that its coefficients and are nothing but the binomial coefficients so we will calculate binomial coefficients of each line and at each index and print them, the coefficient value at every index is nCr where n is equal to the current row number and r is the rth entry in the row n and its value is FACT(n)/(FACT(n-r)*FACT(r)) where FACT(X) is the factorial of the number X but in this approach, we will use maths to derive the relation between Eth entry ‘RCE’ and (E-1)th entry RC(E-1) 

#     So RCE and  RC(E-1)
#     RCE = FACT(R)/(FACT(R-E)*FACT(E)) and RC(E-1)= FACT(R)/(FACT(R-E+1)*FACT(E-1)) after simplifying and comparing we get
#     RCE = RC(E-1) * (R-E+1)/E.
#     Declare an ArrayList of ArrayList TRIANGLE to store the values of the elements.
#     Now run a loop from row R=1 to R=N.
#     Inside this initialize RCE=1 that represents rCe.
#     Inside this loop run a loop from entry E=1 till entry E=R. Store RCE in the ArrayList and update RCE to RCE*(ROW - E)/E.
#     Finally, return ArrayList.

# Time Complexity

# O(N^2), Where ‘N’ denotes the number of Rows.

# because we are using two nested loops.

'''
	Time Complexity: O(N^2)
	Space complexity: O(1)
	
	Where N denotes the number of Rows.
'''

def printPascal(n):
    
    triangle = []
    
    for row in range(1, n+1):
        
        rCe = 1
        add = []
        
        for i in range(1, row+1):
            
            add.append(rCe)
            rCe = rCe * (row - i) // i
            
        triangle.append(add)
        
    return triangle

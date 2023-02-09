# Given a positive integer N, return the Nth row of pascal's triangle.
# Pascal's triangle is a triangular array of the binomial coefficients formed by 
# summing up the elements of previous row.

# Example :
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# For N = 3, return 3rd row i.e 1 2 1

# Example 1:

# Input:
# N = 4
# Output: 1 3 3 1
# Explanation: 4th row of pascal's triangle
# is 1 3 3 1.

# Example 2:

# Input:
# N = 5
# Output: 1 4 6 4 1
# Explanation: 5th row of pascal's triangle
# is 1 4 6 4 1.

class Solution:

	def nthRowOfPascalTriangle(self,k):
	    # code here
	    k = k-1
	    li = [1]
	    p = [1,1]
	    for l in range(1,k+1):
	        val = p[0]*(k-l+1)//(p[1]*(l))
	        li.append(val % (10**9+7))
	        p = [p[0]*(k-l+1),p[1]*(l)]
	    return li

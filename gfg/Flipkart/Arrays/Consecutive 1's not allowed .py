# Python program to count
# all distinct binary strings
# without two consecutive 1's

# https://www.youtube.com/watch?v=H7tshfFTSvw
def countStrings(n):

	a=[0 for i in range(n)]
	b=[0 for i in range(n)]
	a[0] = b[0] = 1
	for i in range(1,n):
		a[i] = a[i-1] + b[i-1]
		b[i] = a[i-1]
	
	return a[n-1] + b[n-1]

print(countStrings(3))

class Solution:

	def countStrings(self,n):
    	# code here
    	one = 1
    	zero = 1
    	for i in range(2 , n+1):
    	    newone = zero % 1000000007
    	    newzero = (one + zero) % 1000000007
    	    
    	    one = newone
    	    zero = newzero
    	return (one + zero) % 1000000007
    	
        
# This problem can be solved using Dynamic Programming. 
# Let a[i] be the number of binary strings of length i which do 
# not contain any two consecutive 1’s and which end in 0. Similarly,
# let b[i] be the number of such strings which end in 1.
# We can append either 0 or 1 to a string ending in 0, 
# but we can only append 0 to a string ending in 1.
# This yields the recurrence relation: 

# a[i] = a[i - 1] + b[i - 1]
# b[i] = a[i - 1] 

# The base cases of above recurrence are a[1] = b[1] = 1. 
# The total number of strings of length i is just a[i] + b[i].



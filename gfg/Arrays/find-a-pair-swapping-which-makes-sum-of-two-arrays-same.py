# Given two arrays of integers, find a pair of values (one value from each array) 
# that you can swap to give the two arrays the same sum.
# Examples: 
 

# Input: A[] = {4, 1, 2, 1, 1, 2}, B[] = (3, 6, 3, 3) 
# Output: {1, 3} 
# Sum of elements in A[] = 11 
# Sum of elements in B[] = 15 
# To get same sum from both arrays, we 
# can swap following values: 
# 1 from A[] and 3 from B[]
# Input: A[] = {5, 7, 4, 6}, B[] = {1, 2, 3, 8} 
# Output: 6 2

# Naive
# Python code naive solution to find a pair swapping
# which makes sum of lists sum.


# Function to prints elements to be swapped
def findSwapValues(A,B):
	# Calculation if sums from both lists
	sum1=sum(A)
	sum2=sum(B)

	# Boolean variable used to reduce further iterations
	# after the pair is found
	k=False

	# Lool for val1 and val2, such that
	# sumA - val1 + val2 = sumB -val2 + val1
	val1,val2=0,0
	for i in A:
		for j in B:
			newsum1=sum1-i+j
			newsum2=sum2-j+i
			
			if newsum1 ==newsum2:
				val1=i
				val2=j
				# Set to True when pair is found
				k=True
				break
		# If k is True, it means pair is found.
		# So, no further iterations.
		if k==True:
			break
	print (val1,val2)
	return


# Driver code
A=[4,1,2,1,1,2]
B=[3,6,3,3]

# Call to function
findSwapValues(A,B)

# We are looking for two values, a and b, such that: 
# sumA - a + b = sumB - b + a
#     2a - 2b  = sumA - sumB
#       a - b  = (sumA - sumB) / 2

# Python code for optimized implementation

def findSwapValues(a, n, b, m):
    # Your code goes here
    
    s1 = sum(a)
    s2 = sum(b)
    a.sort()
    b.sort()

    
    i = 0
    j = 0
    
    while i < n and j < m:
        p = s1 - a[i] + b[j]
        q = s2 - b[j] + a[i]
        if (p == q):
            return 1
        if (p > q):
            i+=1
        else:
            j+=1
    return -1
                


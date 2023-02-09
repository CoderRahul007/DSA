# Problem Statement
# You are given a three integers 'X', 'N', and 'M'. Your task is to find ('X' ^ 'N') % 'M'.
#  A ^ B is defined as A raised to power B and A % C is the remainder when A is divided by C.
# Input format :

# The first line of input contains a single integer 'T', representing the number of test cases. 

# The first line of each test contains three space-separated integers 'X', 'N', and 'M'.

# Output format :

# For each test case, return a single line containing the value of ('X' ^ 'N') % 'M'.

# Note:

# You don't need to print anything, it has already been taken care of. Just implement the given function.

#############################################################################################################

#  Recursive Approach

# In this solution, we will use the below property: 
                         
# So we will use recursion to calculate ‘X’ ^ ‘N’ by dividing ‘N’ into two equal parts in each recursive call. 
 
#  The Steps are as follows:
 
# Declare a function modularExponentiation which has three arguments ‘X’, ‘N’, and ‘M’.
# If ‘N’ == 0 then return 1.
# Calculate ‘X’ ^ ('N' / 2) recursively and store it in ‘ANSWER’ variable i.e. do ‘ANSWER’ = modularExponentiation('X', ‘N’ / 2, ‘M’).
# If ‘N’ is even then return the square of answer i.e. return ('ANSWER' * ‘ANSWER’) % ‘M’.
# Else return the square of answer multiplied with X i.e. return ((‘ANSWER’ * ‘ANSWER’) % ‘M’  * ‘X’ % ‘M’) % ‘M’.

# Time Complexity

# O(log N), Where ‘N’ is the number given in the problem.
 
# Since we require O(log N) steps to reach the base case i.e. make N = 0. Hence the overall time complexity will be O(log N). 
# Space Complexity

# O(log N), Where ‘N’ is the number given in the problem. 

# Since we will require O(log N) recursive calls. Hence the overall space complexity will be O(log N).

"""
	Time Complexity  : O(log N)
	Space Complexity : O(log N)

	Where 'N' is the number given in the problem.
"""

def modularExponentiation(x, n, m):
	# Base case.
	if (n == 0):
		return 1
	
	# Calculate 'X' ^ ('N' / 2) recursively and store it in ans variable.
	answer = modularExponentiation(x, n // 2, m)

	# If 'N' is even then return the square of answer.
	if (n % 2 == 0):
		return (answer * answer) % m
	# Else return the square of answer multiplied with 'X.
	else:
		return ((((answer * answer) % m) * x) % m) % m
	
# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1


######################################################################################################################

# In this solution, we will use binary exponentiation.  
# The idea here is to split ‘N’ in powers of two by converting it into its binary representation to achieve answer in O(log ‘N’) steps. 
# For example if ‘N’ = 7 and ‘X’ = 8. The binary representation of ‘N’ = 111. So 8^7 can be calculated using multiplication 8^4 , 8^2, 8. 
# So in each step, we will keep squaring ‘X’ and if ‘N’ has a set bit its binary representation then we will multiply ‘X’ to answer. 
# The Steps are as follows: 
# Declare a variable to store our result, say ‘ANSWER’, and initialize it with 1.
# Run a loop until ‘N’ > 0, and do:
# If bitwise and of ‘N’ with 1 is 1 then multiply the answer with ‘X’.
# Do modular squaring of 'X' i.e. do 'X' = ('X' * 'X') % 'M'.
# Finally, return the ‘ANSWER’.
# Time Complexity
# O(log N), Where ‘N’ is the number given in the problem.
# Since we are running a loop that takes O(logN) time in the worst case.
#  Hence the overall time complexity will be O(log N). 
# Space Complexity
# O(1).
# Since constant space is required and hence the space complexity will be O(1).

def modularExponentiation(x, n, m):
	# Write your code here.
    ans = 1
    xx = x
    while n > 0:
        if n % 2 == 0:
            xx = (xx % m * xx % m) % m
            n = n >> 1 # div by 2
        else: # at last the n will be 1 so it will se executed
            ans = (ans * xx % m) % m
            n = n-1
    return ans % m


"""
	Time Complexity  : O(log N)
	Space Complexity : O(1)

	Where 'N' is the number given in the problem.
"""

def modularExponentiation(x, n, m):
	# Declare a variable to store our result and initialize it with 1.
	answer = 1

	# Run a loop until 'N' > 0.
	while (n > 0):
		# If bitwise and of 'N' with 1 is 1 then multiply answer with 'X'.
		if (n & 1): # if odd
			answer = (answer * x) % m
		
		# Do modular squaring of 'X'.
		x = (x * x ) % m

		# Right shift 'N' by 1 bit for next iteration.
		n >>= 1

	return answer

# Main.
t = int(input())
while (t > 0):
	lst = list(map(int,input().split()))
	x,n,m = lst[0], lst[1], lst[2]
	print(modularExponentiation(x, n, m))
	t -= 1
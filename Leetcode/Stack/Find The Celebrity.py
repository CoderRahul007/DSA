# In a party of N people, only one person is known to everyone. Such a person may be 
# present at the party, if yes, (s)he doesn’t know anyone at the party. We can only ask
#  questions like “does A know B? “. Find the stranger (celebrity) in the minimum number of questions.
# We can describe the problem input as an array of numbers/characters representing persons
#  in the party. We also have a hypothetical function HaveAcquaintance(A, B) which returns true 
#  if A knows B, and false otherwise. How can we solve the problem? 

# Examples:  

# Input:
# MATRIX = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 0, 0, 0}, {0, 0, 1, 0} }
# Output: id = 2
# Explanation: The person with ID 2 does not know anyone but everyone knows him

# Input:
# MATRIX = { {0, 0, 1, 0}, {0, 0, 1, 0}, {0, 1, 0, 0}, {0, 0, 1, 0} }
# Output: No celebrity
# Explanation: There is no celebrity.

############################## The Celebrity Problem using Elimination Technique:
# Some observations are based on elimination technique (Refer to Polya’s How to Solve It book). 

# If A knows B, then A can’t be a celebrity. Discard A, and B may be celebrity.
# If A doesn’t know B, then B can’t be a celebrity. Discard B, and A may be celebrity.
# Repeat above two steps till there is only one person.
# Ensure the remained person is a celebrity. (What is the need of this step?)
# Follow the steps below to solve the problem:

# Create a stack and push all the ids in the stack.
# Run a loop while there are more than 1 element in the stack.
# Pop the top two elements from the stack (represent them as A and B)
# If A knows B, then A can’t be a celebrity and push B in the stack.
#  Else if A doesn’t know B, then B can’t be a celebrity push A in the stack.
# Assign the remaining element in the stack as the celebrity.
# Run a loop from 0 to n-1 and find the count of persons who knows the celebrity 
# and the number of people whom the celebrity knows.
# If the count of persons who knows the celebrity is n-1 and the count of people 
# whom the celebrity knows is 0 then return the id of the celebrity else return -1.

N = 8
 
# Person with 2 is celebrity
MATRIX = [[0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 0, 0],
          [0, 0, 1, 0]]
        
def knows(a , b):
    return M[a][b]

def findCelebrity(n):
    stack = [i for i in range(n)]
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()

        if knows(a, b):
            stack.append(b)
        else:
            stack.append(a)
    if len(stack) == 0:
        return -1
    c = stack.pop() # potential candidate
    for i in range(n):
        if (i != c and (knows(c, i) or not knows(i, c))):
            return -1
    return c

# Time Complexity: O(N), The total number of comparisons is 3(N-1).
# Auxiliary Space: O(N), n extra space is needed to store the stack


#######################################################################################
# The Celebrity Problem using Two-pointer approach:
# The idea is to use two pointers, one from start and one from the end. Assume the start person is A, 
# and the end person is B. If A knows B, then A must not be the celebrity. Else, B must not be the celebrity.
#  At the end of the loop, only one index will be left as a celebrity. Go through each person again and check 
#  whether this is the celebrity. 
# The Two Pointer approach can be used where two pointers can be assigned, one at the start and 
# the other at the end, and the elements can be compared and the search space can be reduced. 
 

# Follow the steps below to solve the problem:

# Create two indices i and j, where i = 0 and j = n-1
# Run a loop until i is less than j.
# Check if i knows j, then i can’t be a celebrity. so increment i, i.e. i++
# Else j cannot be a celebrity, so decrement j, i.e. j–
# Assign i as the celebrity candidate
# Now at last check whether the candidate is actually a celebrity by re-running a loop
#  from 0 to n-1  and constantly checking if the candidate knows a person or if there is a
#   candidate who does not know the candidate.
# Then we should return -1. else at the end of the loop, we can be sure that the candidate 
# is actually a celebrity.

 # Python3 code
class Solution:

	# Function to find if there is a celebrity in the party or not.
	# return index if celebrity else return -1
	def celebrity(self, M, n):
		# code here
		i = 0
		j = n-1
		candidate = -1
		while(i < j):
			if M[j][i] == 1:
				j -= 1
			else:
				i += 1

		candidate = i
		for k in range(n):
			if candidate != k:
				if M[candidate][k] == 1 or M[k][candidate] == 0:
					return -1

		return candidate


n = 4
m = [[0, 0, 1, 0],
	[0, 0, 1, 0],
	[0, 0, 0, 0],
	[0, 0, 1, 0]]
ob = Solution()
a = ob.celebrity(m, n)
if a == -1:
	print("No Celebrity")
else:
	print("Celebrity ID", a)


# Time Complexity: O(N), Iterating two times the array of size N.
# Auxiliary Space: O(1) No extra space is required.
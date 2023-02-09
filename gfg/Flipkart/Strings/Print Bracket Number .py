class Solution:
	def barcketNumbers(self, S):
		# code here
		st = []
		res = []
		count = 0
		for i in S:
		    if i in "(":
		        count+=1
		        st.append(count)
		        res.append(st[-1])
		    elif i in ")":
		        res.append(st[-1])
		        st.pop()
		return res


# Given a string S, the task is to find the bracket numbers. 

# Example 1:

# Input:  S = "(aa(bdc))p(dee)â€‹"
# Output: 1 2 2 1 3 3
# Explanation: The highlighted brackets in
# the given string (aa(bdc))p(dee) has been 
# assigned the numbers as: 1 2 2 1 3 3.

# Example 2:

# Input:  S = "(((()("
# Output: 1 2 3 4 4 5
# Explanation: The highlighted brackets in
# the given string (((()( has been assigned
# the numbers as: 1 2 3 4 4 5

# Given an input stream of A of n characters consisting only of lower case alphabets.
#  The task is to find the first non repeating character, each time a character is 
# inserted to the stream. If there is no such character then append '#' to the answer.
 

# Example 1:

# Input: A = "aabc"
# Output: "a#bb"
# Explanation: For every character first non
# repeating character is as follow-
# "a" - first non-repeating character is 'a'
# "aa" - no non-repeating character so '#'
# "aab" - first non-repeating character is 'b'
# "aabc" - first non-repeating character is 'b'

# Example 2:

# Input: A = "zz"
# Output: "z#"
# Explanation: For every character first non
# repeating character is as follow-
# "z" - first non-repeating character is 'z'
# "zz" - no non-repeating character so '#'

class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		flag = [0]*26
		ans = []
		q = []
		for v in A:
		    i = ord(v) - ord('a')
		    q.append(v)
		    flag[i]+=1
		    while q :
		        j = ord(q[0]) - ord('a')
		        if flag[j] > 1:
		            q.pop(0)
		        else:
		            ans.append(q[0])
		            break
		    if not q:
		        ans.append('#')
		       
		return ''.join(ans)
#Input:   str1 = "geek",  str2 = "eke"
# Output: 5
# Explanation: 
# String "geeke" has both string "geek" 
# and "eke" as subsequences.

# Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
# Output:  9
# Explanation: 
# String "AGXGTXAYB" has both string 
# "AGGTAB" and "GXTXAYB" as subsequences.

# Length of the shortest supersequence  
# = (Sum of lengths of given two strings) 
# - (Length of LCS of two given strings) 

# Add LCS char only once
# Assume 1st common char belongs to LCS char
# Add non lcs char in order of S1 or S2

# Python implementation to find shortest string for
# a combination of two strings

def SCS(str1 , str2):
	m = len(str1)
	n = len(str2) 
	
	# construct the dp table
	t = [[0 for j in range(n + 1)] for i in range(m + 1)]
	for i in range(1, m+1):
		for j in range(1, n+1):
			if str1[i-1] == str2[j-1]:
				t[i][j] = 1 + t[i-1][j-1]
			else:
				t[i][j] = max(t[i-1][j], t[i][j-1])
		
		

	i = len(str1)
	j = len(str2)
	
	string = ''
	
	while i>0 and j>0:
		if str1[i-1] == str2[j-1]:
			string += str1[i-1]
			i -= 1
			j -= 1
		else:
			if t[i][j-1] > t[i-1][j]:
				string += str2[j-1]  # in lcs we dont do this
				j -= 1
			else:
				string += str1[i-1] # in lcs we dont do this
				i -= 1
	# now atleast ome string must have been exhausted
	# so for remaining string

	print(string[::-1])
	
	
	# if str1 is remaining
	while i>0:
		string += str1[i-1]
		i -= 1
	
	# if str2 is remaining
	while j>0:
		string += str2[j-1]
		j -= 1
	
	return string[::-1]	


# Driver code
a = "algorithm"
b = "rhythm"
size_a = len(a)
size_b = len(b)
print(SCS(a, b))

# It follows from the above that in order to find the SCS, we first need to find the longest common subsequence (LCS)
# between the two strings. Having found the LCS, we compare each character in the input strings with a character
# in the LCS; let's call these characters 'x', 'y' and 'z', respectively. If all three characters are the same,
# then we found a character from the LCS, and it is appended to the SCS. If only one of 'x' and 'y' is the same as 'z',
# then we append the character that is NOT equal to the SCS (like 'a' and 'd' in the example above). If none of 'x' or
# 'y' is equal to 'z', both are appended to the SCS. At the end, we append the remaining characters from the strings
# to the SCS.

# Note that if only the length of the SCS is required, we don't need to reconstruct the SCS, the length is simply
# given by len(s1) + len(s2) - len(LCS).

# Time complexity: O(mn) to find the LCS, where m = len(s1) and n = len(s2), plus O(m) + O(n) since we check all
# characters of the two strings.
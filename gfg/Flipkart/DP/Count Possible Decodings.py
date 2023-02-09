# Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, 
# count the number of possible decodings of the given digit sequence. 

# Examples: 

# Input:  digits[] = "121"
# Output: 3
# // The possible decodings are "ABA", "AU", "LA"

# Input: digits[] = "1234"
# Output: 3
# // The possible decodings are "ABCD", "LCD", "AWD"
# An empty digit sequence is considered to have one decoding. 
# It may be assumed that the input contains valid digits from 0 to 9 and 
# there are no leading 0’s, no extra trailing 0’s, and no two or more consecutive 0’s.

# This problem is recursive and can be broken into sub-problems. We start
#  from the end of the given digit sequence. We initialize the total count
#  of decodings as 0. We recur for two subproblems. 
# 1) If the last digit is non-zero, recur for the remaining (n-1) digits 
# and add the result to the total count. 
# 2) If the last two digits form a valid character (or smaller than 27), 
# recur for remaining (n-2) digits and add the result to the total count.

# Following is the implementation of the above approach.  
# Recursive implementation of numDecodings
def numDecodings(s: str) -> int:
	if len(s) == 0 or (len(s) == 1
		and s[0] == '0'):
		return 0
	return numDecodingsHelper(s, len(s))


def numDecodingsHelper(s: str, n: int) -> int:
	if n == 0 or n == 1:
		return 1
	count = 0
	if s[n-1] > "0":
		count = numDecodingsHelper(s, n-1)
	if (s[n - 2] == '1'
		or (s[n - 2] == '2'
			and s[n - 1] < '7')):
		count += numDecodingsHelper(s, n - 2)
	return count


# Driver code
digits = "1234"
print("Count is ", numDecodings(digits))

# https://www.youtube.com/watch?v=cQX3yHS0cLo

class Solution:

	def CountWays(self, s):
		# Code here
	    n = len(s)
	    if n == 0 or s[0] == '0' :
	        return 0
	    if n == 1:
	        return 1
	    mod = 1000000007
	    c1 = 1 # previous to previous pointer
	    c2 = 1 # previous pointer
	    for i in range(1 , n):
	        d = int(s[i])
	        dd = int(s[i-1]) * 10 + d
	        c = 0
	        if d > 0:
	            c+= c2
	        if dd >= 10 and dd <= 26:
	            c+= c1
	        c1 = c2 % mod
	        c2 = c % mod
	    return c2

#####################################
    #    int n = str.size();
    #     const int mod = 1e9 + 7;

    #     // A table to store results of subproblems
    #     int count[n + 1];
    #     count[0] = 1;
    #     count[1] = 1;

    #     //for base condition "01123" should return 0
    #     if (str[0] == '0')
    #         return 0;

    #     for (int i = 2; i <= n; i++)
    #     {
    #         count[i] = 0;

    #         // If the last digit is not 0, then last digit must add to the number of words
    #         if (str[i - 1] > '0')
    #             count[i] = count[i - 1] % mod;


    #         // If second last digit is smaller than 2 and last digit is smaller than 7, then last two digits form a valid character
    #         if (str[i - 2] == '1' || (str[i - 2] == '2' && str[i - 1] < '7'))
    #             count[i] = (count[i] + count[i - 2]) % mod;
    #     }
    #     return count[n];


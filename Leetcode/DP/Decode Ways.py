# A message containing letters from A-Z can be encoded into numbers using the following mapping:

# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into
# letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

# Given a string s containing only digits, return the number of ways to decode it.

# The test cases are generated so that the answer fits in a 32-bit integer.


# Example 1:

# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
# Example 3:

# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


# https://leetcode.com/problems/decode-ways/solutions/30592/dp-solution-with-detailed-explanation-python-sample-code/?languageTags=python



##################################################################################
# Recursion

# Recursive implementation of numDecodings

# This problem is recursive and can be broken into sub-problems. We start from the end of the given digit sequence.
#  We initialize the total count of decodings as 0. We recur for two subproblems. 
# 1) If the last digit is non-zero, recur for the remaining (n-1) digits and add the result to the total count. 
# 2) If the last two digits form a valid character (or smaller than 27), recur for remaining (n-2) digits and add the result to the total count.

# Following is the implementation of the above approach.  

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
    if (s[n - 2] == '1' or (s[n - 2] == '2' and s[n - 1] < '7')):
        count += numDecodingsHelper(s, n - 2)
    return count


# Driver code
digits = "1234"
print("Count is ", numDecodings(digits))
# This code is contributed by Frank Hu


###################################################################################
# Memoization
def numDecodings(self, s: str) -> int:
    validNums = {str(i) for i in range(1, 27)}
    n = len(s)
    memo = {}

    return self.recursion(s, 0, validNums, n, memo)


def recursion(self, s, i, validNums, n, memo):
    if i in memo:
        return memo[i]

    if i == n:
        return 1

    if s[i] == '0':
        return 0

    ans1 = ans2 = 0

    if s[i] in validNums:
        ans1 = self.recursion(s, i + 1, validNums, n, memo)

    if i < n - 1 and (s[i] + s[i + 1]) in validNums:
        ans2 = self.recursion(s, i + 2, validNums, n, memo)

    memo[i] = ans1 + ans2

    return memo[i]

#####################################################################################
# Using O 1 space


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        validSet = set([str(x) for x in range(1,27)])
        
        a,b = 0, 1
        if s[-1] in validSet:
            a = 1
        for i in range(n-2,-1,-1):
            tmp = a
            if s[i] not in validSet:
                # a = 0
                tmp = 0
            if s[i:i+2] in validSet:
                tmp += b
            a,b = tmp,a
        return a
        
        

##################################################################################
# DP


# A Dynamic Programming based Python3
# implementation to count decodings

# A Dynamic Programming based function
# to count decodings
def countDecodingDP(digits, n):

	count = [0] * (n + 1); # A table to store
						# results of subproblems
	count[0] = 1;
	count[1] = 1;

	for i in range(2, n + 1):

		count[i] = 0;

		# If the last digit is not 0, then last
		# digit must add to the number of words
		if (digits[i - 1] > '0'):
			count[i] = count[i - 1];

		# If second last digit is smaller than 2
		# and last digit is smaller than 7, then
		# last two digits form a valid character
		if (digits[i - 2] == '1' or
		(digits[i - 2] == '2' and
			digits[i - 1] < '7') ):
			count[i] += count[i - 2];

	return count[n];

# Driver Code
digits = "1234";
n = len(digits);
print("Count is" ,
	countDecodingDP(digits, n));


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 2)
        dp[n+1] = 1
        dp[n] = 1
        
        for i in range(n-1, -1, -1):
            two_digit = int(s[i:i+2])
            if s[i] == "0":
                dp[i] = 0
            elif two_digit >= 10 and two_digit <= 26:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = dp[i+1]
                
        return dp[0]
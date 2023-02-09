# https://www.geeksforgeeks.org/minimum-number-of-squares-whose-sum-equals-to-given-number-n/

# A naive recursive Python program to
# find minimum number of squares whose
# sum is equal to a given number

# Returns count of minimum squares
# that sum to n
def getMinSquares(n):

	# base cases
	if n <= 3:
		return n;

	# getMinSquares rest of the table
	# using recursive formula
	# Maximum squares required
	# is n (1 * 1 + 1 * 1 + ..)
	res = n

	# Go through all smaller numbers
	# to recursively find minimum
	for x in range(1, n + 1):
		temp = x * x;
		if temp > n:
			break
		else:
			res = min(res, 1 + getMinSquares(n
								- temp))
	
	return res;

# Driver code
print(getMinSquares(6))

# This code is contributed by nuclode
# A dynamic programming based Python
# program to find minimum number of
# squares whose sum is equal to a
# given number
from math import ceil, sqrt

# Returns count of minimum squares
# that sum to n
def getMinSquares(n):

	# Create a dynamic programming table
	# to store sq and getMinSquares table
	# for base case entries
	dp = [0, 1, 2, 3]

	# getMinSquares rest of the table
	# using recursive formula
	for i in range(4, n + 1):
		
		# max value is i as i can always
		# be represented as 1 * 1 + 1 * 1 + ...
		dp.append(i)

		# Go through all smaller numbers
		# to recursively find minimum
		for x in range(1, int(ceil(sqrt(i))) + 1):
			temp = x * x;
			if temp > i:
				break
			else:
				dp[i] = min(dp[i], 1 + dp[i-temp])

	# Store result
	return dp[n]

# Driver code
print(getMinSquares(6))

# This code is contributed by nuclode
import sys
def minCount(n):
	minSquaresRequired = [0 for i in range(n+1)];

	minSquaresRequired[0] = 0;

	minSquaresRequired[1] = 1;

	for i in range(2,n+1):

		minSquaresRequired[i] = sys.maxsize;
		j = 1

		for j in range(1,i - (j * j)):
			if(i - (j * j) >= 0):
				minSquaresRequired[i] = min(minSquaresRequired[i], minSquaresRequired[i - (j * j)]);
			else:
				break
		

		minSquaresRequired[i] += 1;
	
	result = minSquaresRequired[n];

	return result;

# Driver code
if __name__ == '__main__':
	print(minCount(6));


# This code is contributed by umadevi9616
